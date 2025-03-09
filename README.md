# 🧠 **Instruction Classification**

## 📜 **Project Overview**
This project involves training and deploying a BERT-based model to classify following instructions types into predefined categories. The system uses a Flask-based front end to allow users to input new instructions and get real-time classifications.

    Simple instruction
    Instruction with Sequence
    Instruction with Options
    Mandatory Instruction
    Instruction with Goal
    Instruction with Reason
    Negative Instruction
    Non Instruction


## 📊 **Dataset**
- **Primary Dataset**: `wikihow.csv` containing instructions classified into 6 different categories.
- **Test Datasets**:
  - **NCERT Data**: Contains academic-style instructions.
  - **TNSB Data**: Includes practical, step-based instructions.
  - **Pixel_help Data**: Comprises technical instructions for device usage.

### Product Screenshot
![image](https://github.com/user-attachments/assets/45358c0e-b98e-4829-8c19-756135a68713)


### Dataset Screenshot
![image](https://github.com/user-attachments/assets/4d6699fc-fb3f-4346-83ae-baf21cbbd7a5)


---

## ⚙️ **Model Architecture**
Two models were trained:
1. **Binary Classification Model**: Determines whether a text is an instruction or not.
2. **Multi-Class Classification Model**: Categorizes instructions into one of six classes.

### Training Details:
- The models were trained using the `wikihow.csv` dataset.
- After training, the models were saved as `.pt` files for easy access by the Flask backend.
- The frontend allows users to input instructions, and the backend classifies them using the trained models.

---

## 📈 **Results**
### Accuracy Table
|                | WikiHow | **TNSB**| **NCERT** | **Pixel_help** |
|----------------|---------|---------|-----------|----------------|
| **Binary**     |   99%   |   100%  |     100%  |        100%    |
| **Multi-Class**|   92%   |    99%  |      98%  |        98%     |

### Training Graphs
![binary graph](https://github.com/user-attachments/assets/89962a7a-9357-4253-b55c-35c5e1a54688)
![multi graph](https://github.com/user-attachments/assets/95e362c0-b092-4373-b417-027eb974be8f)


### Classification Reports\

#### **Binary Classification**
- **TNSB Data**: The binary model achieved an accuracy of 99.8% on practical, step-based instructions.
![pixel binary](https://github.com/user-attachments/assets/068a4858-950b-48a4-a68a-0b2d21918a1e)

- **NCERT Data**: The binary model scored 99.2% on academic-style instructions.
  
![pixel binary](https://github.com/user-attachments/assets/068a4858-950b-48a4-a68a-0b2d21918a1e)


- **Pixel_help Data**: The binary model performed perfectly, achieving 100% accuracy for technical instructions.
![pixel binary](https://github.com/user-attachments/assets/068a4858-950b-48a4-a68a-0b2d21918a1e)

#### **Multi-Class Classification**
- **TNSB Data**: The multi-class model achieved 99% accuracy in classifying practical instructions.
  ![tnsb multti](https://github.com/user-attachments/assets/ad88fabb-fbd1-4ff2-820d-17e24224c018)

- **NCERT Data**: It achieved 98% accuracy for academic-style instructions.

![pixel multi](https://github.com/user-attachments/assets/ae8a4e39-2e15-4c07-80d3-da312ffbf868)

- **Pixel_help Data**: The model performed excellently with 98% accuracy in technical instruction categorization.
![pixel multi](https://github.com/user-attachments/assets/ae8a4e39-2e15-4c07-80d3-da312ffbf868)

## Sample Video
https://github.com/user-attachments/assets/064c88da-85d5-4a83-a753-2f7c34b59975



---

## 💻 **System Workflow**
1. **Model Training**:
   - Preprocess the `wikihow.csv` dataset.
   - Train and save the binary and multi-class models.
2. **Deployment**:
   - Set up a Flask backend to load the trained models.
   - Create a user interface for instruction classification.
3. **Real-Time Classification**:
   - Input new instructions via the frontend.
   - Models classify the instructions and return results.

---

## 📚 **Libraries Used**
- **Deep Learning**: Transformers (Hugging Face), PyTorch
- **Data Processing**: Pandas, NumPy
- **Web Development**: Flask

---

## 🖥️ **System Requirements**
### Hardware:
- **Processor**: Intel Core i5 or higher.
- **RAM**: Minimum 8GB.
- **Storage**: 256GB SSD (minimum).

### Software:
- **Python**: Version 3.x
- **Libraries**: Install dependencies via `pip install -r requirements.txt`

---

## 🚀 **Setup and Usage**
1. **Clone the repository**:
   ```bash
   git clone MIRA-INSTRUCTION-CLASSIFICATION
   cd MIRA-INSTRUCTION-CLASSIFICATION
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```
4. **Access the application**:
   Open `http://127.0.0.1:5000` in your browser.



