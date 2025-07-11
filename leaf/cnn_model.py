import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os


def create_model(input_shape=(224, 224, 3), num_classes=40):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

# training history
def plot_history(history):
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# train the model
def train_model(train_dir, validation_dir, epochs=5, batch_size=36):
    # Data augmentation 
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    #  validation
    validation_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical'
    )

    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical'
    )

    model = create_model(num_classes=len(train_generator.class_indices))

    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // batch_size
    )

    
    plot_history(history)

    return model

# save the model in 'model' folder
def save_model(model, model_path):
    # Create the 'model' directory if it doesn't exist
    if not os.path.exists('model'):
        os.makedirs('model')
        
    model.save(model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    # change it to your dataset path
    train_dir = 'C:/Users/dell/Desktop/minipro/leaf/leafdatav2/train'
    validation_dir = 'C:/Users/dell/Desktop/minipro/leaf/leafdatav2/validation'
    
    trained_model = train_model(train_dir, validation_dir)
    
    # Save model in 'mo/el' directory
    save_model(trained_model, 'model/plant_medicinal_model.h5')


def predict_disease(image_path):
    
    model = tf.keras.models.load_model('model/plant_medicinal_model.h5')
    
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  
    img_array /= 255.  

    predictions = model.predict(img_array)
    
    predicted_class = tf.argmax(predictions[0]).numpy()
    
    class_names = ['Healthy', 'Disease1', 'Disease2', 'Disease3']
    
    return class_names[predicted_class] 