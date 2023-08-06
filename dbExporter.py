import os
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create the root export directory
export_dir = 'export'
os.makedirs(export_dir, exist_ok=True)

# Retrieve books from the database
cursor.execute("SELECT id, book_title FROM books")
books = cursor.fetchall()

for book in books:
    book_id = book[0]
    book_title = book[1]

    # Create the book directory
    book_dir = os.path.join(export_dir, book_title)
    os.makedirs(book_dir, exist_ok=True)

    # Retrieve chapters for the current book
    cursor.execute(f"SELECT id, chapter_number FROM chapters WHERE book_id={book_id}")
    chapters = cursor.fetchall()

    for chapter in chapters:
        chapter_id = chapter[0]
        chapter_number = chapter[1]

        # Create the chapter directory
        chapter_dir = os.path.join(book_dir, f'Chapter {chapter_number}')
        os.makedirs(chapter_dir, exist_ok=True)

        # Retrieve verses for the current chapter
        cursor.execute(f"SELECT verse_number, scripture_text FROM verses WHERE chapter_id={chapter_id}")
        verses = cursor.fetchall()

        for verse in verses:
            verse_number = verse[0]
            scripture_text = verse[1]

            # Create the verse file
            verse_file = os.path.join(chapter_dir, f'Verse {verse_number}.md')
            with open(verse_file, 'w', encoding='utf-8') as f:
                f.write(scripture_text)

# Close the database connection
conn.close()

