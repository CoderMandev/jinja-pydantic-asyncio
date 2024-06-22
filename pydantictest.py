from pydantic import BaseModel
import yaml
from pydantic_core import to_jsonable_python


class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]


my_books = [
		Book(
		    author="J. K. Rowling",
		    title="Harry Potter and the Philosopher's stone",
		    pages=[
		        Page(
		            number=1,
		            text="There once was a boy...",
		        ),
		        Page(
		            number=2,
		            text="He went to magic school...",
		        )
		    ]
		),
		Book(
		    author="Roger Zelazny",
		    title="Lord of Light",
		    pages=[
		        Page(
		            number=1,
		            text="It is said that fifty-three years ago...",
		        )
		    ]
		),
		Book(author="John green",
		    title="Paper Towns",
		    pages=[
		        Page(
		            number=14,
		            text="The longest day of my life began tardily"
                    )    ,
            ]
        ),
]        

print(my_books[0].author)
print(my_books[0].pages[0].text)

for book in my_books:
    print(book.title)


print(yaml.dump(my_books[0].dict()))
print(yaml.dump(to_jsonable_python(my_books)))