from copy_static import copy_static
from generate_pages import generate_pages_recursive


def main():
    print("🚀 Starting static site generation...\n")
    
    copy_static()
    generate_pages_recursive(
        content_dir_path="../content",
        template_path="../template.html",
        dest_dir_path="../public"
    )
    print("\n✅ Static files copied successfully!")
    print("🎉 Site generation complete!")


if __name__ == "__main__":
    main()
