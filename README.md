Virtual Herbal Garden

🌟 Introduction 🌟

The Virtual Herbal Garden is an innovative and immersive platform designed to educate users about medicinal plants. It provides detailed information on each plant, including its botanical and common names, habitat, medicinal uses, and cultivation methods. The platform combines modern technology with traditional knowledge to bridge the gap between ancient herbal practices and contemporary digital solutions. A key feature is the use of image recognition technology, which allows users to identify plants by simply taking pictures.
Installation Guide
Step 1: Clone the repository

    git clone https://github.com/Virtual-Herbal-Garden/.git
    cd leaf

Step 2: Install the dependencies

    pip install -r packages.txt

Step 3: Run the model 

    run cnn_model.py

Step 3: Run the application

    run app.py

Core Technology
The Virtual Herbal Garden system integrates several modern technologies to provide a seamless user experience.
AI & Machine Learning
 * Plant Identification: The core of the system is driven by a Convolutional Neural Network (CNN), a powerful machine learning algorithm well-suited for image recognition tasks. This approach simplifies plant identification, making it faster and more accessible to non-experts.
 * Model Architecture: The CNN model consists of multiple convolutional layers designed to extract features like edges, textures, and colors from plant images. These features are then passed through pooling layers to reduce dimensionality.

![WhatsApp Image 2025-09-04 at 21 09 07](https://github.com/user-attachments/assets/f7c45ed9-782d-4da9-bf07-b91b243924a4)

![WhatsApp Image 2025-09-04 at 21 08 23](https://github.com/user-attachments/assets/cf8d5f08-ff63-4a42-98d8-a9beeb4dabd0)

![WhatsApp Image 2025-09-04 at 21 08 23 (1)](https://github.com/user-attachments/assets/0fb377ae-1da8-4903-8434-3fe350dab7b4)

![WhatsApp Image 2025-09-04 at 21 08 22](https://github.com/user-attachments/assets/6aa5a51f-2b7d-4e07-b052-1da1fb2d5fb6)

![WhatsApp Image 2025-09-04 at 21 08 22 (2)](https://github.com/user-attachments/assets/63b679bb-5c8d-4f17-bf61-c01196c4b1ae)

![WhatsApp Image 2025-09-04 at 21 08 22 (1)](https://github.com/user-attachments/assets/adf482d2-94c7-4274-b84d-88b7e240367c)

![WhatsApp Image 2025-09-04 at 21 08 21](https://github.com/user-attachments/assets/633b8dd5-3a31-4c06-b066-69dad341ea77)

![WhatsApp Image 2025-09-04 at 21 08 21 (2)](https://github.com/user-attachments/assets/97e9b5bc-1ba9-4d80-9025-0cfbcbe686c4)

![WhatsApp Image 2025-09-04 at 21 08 21 (1)](https://github.com/user-attachments/assets/58e4f1ef-9894-4006-bce8-05854cdfeb3b)

   
 * Training: The model is trained on a prepared dataset and evaluated using metrics such as accuracy to ensure reliable results. Image augmentation techniques (e.g., rotations, flipping) are used to prevent overfitting and improve the model's generalizability. The CNN model achieved an accuracy of 85-90%.
![WhatsApp Image 2025-09-04 at 20 36 42](https://github.com/user-attachments/assets/08647c74-5682-4db1-8e6f-915b0be0b3a9)

![WhatsApp Image 2025-09-04 at 20 36 42 (1)](https://github.com/user-attachments/assets/0837284b-1ec2-45ae-8b37-9a19b56c02ba)



 * Frontend: The user interface is built using HTML, CSS, and JavaScript, ensuring cross-device compatibility and an intuitive user experience. Users can upload or take pictures of plants, and the results are dynamically displayed in real-time.
 * Backend: The backend is powered by the Flask web framework, which handles server-side logic and communication between the frontend and the machine learning model. 
Database & Authentication
 * User Authentication: Firebase Authentication is integrated to manage secure user authentication and session handling.
Application Showcase
Web Interface
The web interface is designed to be intuitive and responsive, adapting to different screen sizes.
![WhatsApp Image 2025-09-04 at 20 36 22 (2)](https://github.com/user-attachments/assets/6aac08c8-ef75-403e-be89-321d1ae30c6e)

![WhatsApp Image 2025-09-04 at 20 36 22 (1)](https://github.com/user-attachments/assets/5fcd734b-fdfb-40a3-95f6-046777c039b0)


Plant Detection and Upload Interface
This interface allows users to select and upload an image for identification.
  ![WhatsApp Image 2025-09-04 at 20 36 22](https://github.com/user-attachments/assets/acd3ecb0-10b2-48ff-890a-a5aeb733244d)
Plant Identification in Action
Once an image is processed, the system identifies the plant and provides detailed information.
![WhatsApp Image 2025-09-04 at 20 36 23](https://github.com/user-attachments/assets/b112d2ee-0b4b-4603-a2d5-8ab4e918b15d)


Future Scope
Future plans for the Virtual Herbal Garden include:
 * Building a more interactive platform with 3D models, media, and social elements.
 * Enhancing the platform with better search options and community features to boost user engagement.
 * Integrating gamification to make learning about plants more interactive and fun.
 * Regularly updating the plant database with new plants and information to keep the platform dynamic and serve as a comprehensive information hub.
Contributing
We welcome contributions! Please follow our Contribution Guidelines to get started.
License
This project is licensed under the MIT License - see the LICENSE file for details.
