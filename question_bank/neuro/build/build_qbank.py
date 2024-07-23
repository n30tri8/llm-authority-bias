import fitz  # PyMuPDF
import re
import pandas as pd


def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Iterate over each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text += page.get_text()

    return text


def remove_page_num(text):
    # Define the regex pattern to find new lines with a single number

    # Replace the pattern with an empty string
    processed_text = re.sub(r'^\d+$\n?', '', text, flags=re.MULTILINE)

    return processed_text


def extract_mcqs(text):
    mcqs = []

    # Regular expression to match the questions and answers
    pattern = re.compile(r'(\d+\.\s.*?)(?=\n\d+\.\s|\Z)', re.DOTALL)
    matches = pattern.findall(text)

    for match in matches:
        question_block = match.strip()

        # Split the question block into question and answers
        question_parts = re.split(r'(?=(?:\na\.|\nb\.|\nc\.|\nd\.|\ne\.))', question_block, maxsplit=1)

        if len(question_parts) == 2:
            question = question_parts[0].strip().replace('\n', ' ')
            answers = re.split(r'(?<=\n)(?=\s*[a-e]\.)', question_parts[1].strip())
            answers = [answer.strip().replace('\n', ' ') for answer in answers]
            question = re.sub(r'^[^a-zA-Z"]*', '', question) # remove question number
            # Combine question and answers into a dictionary
            q = {
                'question': question,
                'a': answers[0].strip('a. '),
                'b': answers[1].strip('b. '),
                'c': answers[2].strip('c. '),
                'd': answers[3].strip('d. '),
                'e': answers[4].strip('e. ')
            }
            mcqs.append(q)

    return mcqs

# Path to your PDF file
pdf_path = '/home/filippo/PycharmProjects/llm-authority-bias/question_bank/neuro/source/Esteban Cheng-Ching, Eric P. Baron, Lama Chahine, Alexander Rae- - Comprehensive Review in Clinical Neurology (2016, LWW).pdf'  # Replace with your actual PDF file path

# Extract text
extracted_text = extract_text_from_pdf(pdf_path)

# Remove single number new lines
processed_text = remove_page_num(extracted_text)

# Extract the MCQs
mcqs = extract_mcqs(processed_text)

# Print the extracted MCQs
for mcq in mcqs:
    if(" Questions " in mcq['e']):
            mcq['e'] = mcq['e'].split(" Questions ")[0]

df = pd.DataFrame(mcqs)
df.to_csv('/home/filippo/PycharmProjects/llm-authority-bias/question_bank/neuro/question_bank.csv', index=False)

# Save the extracted text to a file (optional)
#with open('/mnt/data/extracted_text.txt', 'w') as text_file:
#    text_file.write(extracted_text)

print("Text extraction complete. Check the extracted_text.txt file.")