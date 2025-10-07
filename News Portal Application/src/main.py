from services.article_service import ArticleService
from services.user_service import UserService
from services.category_service import CategoryService
from services.tag_service import TagService
from services.comment_service import CommentService
from services.author_service import AuthorService
from services.article_tag_service import ArticleTagService

def menu():
    print("\n=== CMS MENU ===")
    print("1. Manage Users")
    print("2. Manage Authors")
    print("3. Manage Articles")
    print("4. Manage Categories")
    print("5. Manage Tags")
    print("6. Manage Comments")
    print("7. Manage Article Tags")
    print("0. Exit")
    return input("Enter choice: ")

# Initialize services
article_service = ArticleService()
user_service = UserService()
category_service = CategoryService()
tag_service = TagService()
comment_service = CommentService()
author_service = AuthorService()
article_tag_service = ArticleTagService()

def manage_users():
    print("\n--- Users ---")
    print("1. Create User")
    print("2. List Users")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        user = user_service.create_user(name, email)
        print("Created:", user)
    elif choice == "2":
        users = user_service.get_all_users()
        for u in users:
            print(u)

def manage_authors():
    print("\n--- Authors ---")
    print("1. Create Author")
    print("2. List Authors")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        author = author_service.create_author(name, email)
        print("Created:", author)
    elif choice == "2":
        authors = author_service.get_all_authors()
        for a in authors:
            print(a)

def manage_articles():
    print("\n--- Articles ---")
    print("1. Create Article")
    print("2. List Articles")
    choice = input("Choice: ")
    if choice == "1":
        title = input("Title: ")
        content = input("Content: ")
        author_id = int(input("Author ID: "))
        article = article_service.create_article(title, content, author_id)
        print("Created:", article)
    elif choice == "2":
        articles = article_service.get_all_articles()
        for a in articles:
            print(a)

def manage_categories():
    print("\n--- Categories ---")
    print("1. Create Category")
    print("2. List Categories")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        description = input("Description: ")
        category = category_service.create_category(name, description)
        print("Created:", category)
    elif choice == "2":
        categories = category_service.get_all_categories()
        for c in categories:
            print(c)

def manage_tags():
    print("\n--- Tags ---")
    print("1. Create Tag")
    print("2. List Tags")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        tag = tag_service.create_tag(name)
        print("Created:", tag)
    elif choice == "2":
        tags = tag_service.get_all_tags()
        for t in tags:
            print(t)

def manage_comments():
    print("\n--- Comments ---")
    print("1. Create Comment")
    print("2. List Comments by Article ID")
    choice = input("Choice: ")
    if choice == "1":
        article_id = int(input("Article ID: "))
        user_id = int(input("User ID: "))
        content = input("Content: ")
        comment = comment_service.create_comment(article_id, user_id, content)
        print("Created:", comment)
    elif choice == "2":
        article_id = int(input("Article ID: "))
        comments = comment_service.get_comments_by_article(article_id)
        for c in comments:
            print(c)

def manage_article_tags():
    print("\n--- Article Tags ---")
    print("1. Add Tag to Article")
    print("2. Remove Tag from Article")
    print("3. List Tags for Article")
    choice = input("Choice: ")
    if choice == "1":
        article_id = input("Article ID: ")
        tag_id = input("Tag ID: ")
        at = article_tag_service.add_tag_to_article(article_id, tag_id)
        print("Added:", at)
    elif choice == "2":
        article_id = input("Article ID: ")
        tag_id = input("Tag ID: ")
        result = article_tag_service.remove_tag_from_article(article_id, tag_id)
        print("Removed:", result)
    elif choice == "3":
        article_id = input("Article ID: ")
        tags = article_tag_service.get_tags_for_article(article_id)
        print("Tags:", tags)

# --- Main Loop --- #
if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            manage_users()
        elif choice == "2":
            manage_authors()
        elif choice == "3":
            manage_articles()
        elif choice == "4":
            manage_categories()
        elif choice == "5":
            manage_tags()
        elif choice == "6":
            manage_comments()
        elif choice == "7":
            manage_article_tags()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
