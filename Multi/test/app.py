from flask import Flask, render_template, url_for, request, redirect,session, flash
import openpyxl

app = Flask(__name__)

app.secret_key = "sasfuoify8oiuuuuuuuuuuuiuoewurwiurw23bj32lj4kb2k"




@app.route("/",methods=["GET","POST"])
def test():
    
    data=[]

    import torch
    from transformers import BertTokenizer, BertForSequenceClassification

    # Load the saved model and tokenizer
    model_path = "new model"

    model = BertForSequenceClassification.from_pretrained(model_path)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Move the model to the appropriate device (GPU or CPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()  # Set model to evaluation mode

    if request.method == "POST":
        
        new = request.form.get("new")
        print(new)

        
        def preprocess_text(texts, tokenizer, max_len=128):
            input_ids = []
            attention_masks = []

            for text in texts:
                encoded_dict = tokenizer.encode_plus(
                    text,
                    add_special_tokens=True,
                    max_length=max_len,
                    padding='max_length',
                    return_attention_mask=True,
                    return_tensors='pt'
                )

                input_ids.append(encoded_dict['input_ids'])
                attention_masks.append(encoded_dict['attention_mask'])

            return torch.cat(input_ids, dim=0), torch.cat(attention_masks, dim=0)

        def classify_text(model, tokenizer, texts):
            input_ids, attention_masks = preprocess_text(texts, tokenizer)
            input_ids, attention_masks = input_ids.to(device), attention_masks.to(device)

            with torch.no_grad():
                outputs = model(input_ids=input_ids, attention_mask=attention_masks)
                logits = outputs.logits
                _, predictions = torch.max(logits, dim=1)

            return predictions.cpu().numpy()

        # Example usage
        texts = new.split('\n')
        predictions = classify_text(model, tokenizer, texts)
        print(predictions)
        data = zip(texts, predictions)
         # Print predictions
        type_map = {
            1: "Simple instruction | Vidhi (विधि)",
            2: "Mandatory instruction | Samuccaya (समुच्चय)",
            3: "Instruction with option | Vikalpa (विकल्प)",
            4: "Instruction with purpose | Phalavidhi (फलविधि)",
            5: "Instruction with sequence | Śrutikrama (श्रुतिक्रम)",
            6: "Negative instruction | Niṣedha (निषेध)",
            7: "Instruction with reason | Hetu-Hetumadbhāva (हेतु-हेतुमद्भाव)",
            0: "Non instruction | Anavadhāna (अनवधान)"
        }
        types = [type_map.get(pred, "Non instruction | Anavadhāna (अनवधान)") for text, pred in data]
        data = zip(texts,types)

        # Print predictions
        for text, prediction in zip(texts, types):
            print(f'Text: {text} | Prediction: {prediction}')

    return render_template("check.html",data=data)

if __name__ == "__main__":
    app.run(debug=True, port=9000)