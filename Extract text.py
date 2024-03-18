import PyPDF2

# Open the PDF file
with open(r'C:\UMBC\SEMS\2.SEM2\603 Platforms for Big Data Processing\assignment\AS-02\Harry_Potter_(www.ztcprep.com).pdf','rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages) # calculating number of pages in the PDF

    # Date of Birth 13-DEC-1996
    birth_month = 12
    birth_date = 13
    birth_year = 1996

    book_page = 4797  # 6th book is the desired one as per my date of birth
    birth_date_page = birth_date # setting the page number for birth date

    birth_year_page = int(str(birth_year % 100).zfill(2))  # setting the page number for birth year

    # Extracting text as per the date of birth as files 1 and 2 respectively
    with open('file1.txt', 'w') as file1, open('file2.txt', 'w') as file2:
        # Extracting text with respect to birth date
        for page_num in range(4797+birth_date_page, 4797+birth_date_page+11):
            page = pdf_reader.pages[page_num]
            file1.write(page.extract_text())

        # Extracting text with respect to birth year
        for page_num in range(4797+birth_year_page, 4797+birth_year_page+11):
            page = pdf_reader.pages[page_num]
            file2.write(page.extract_text())
