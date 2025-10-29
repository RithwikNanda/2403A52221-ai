html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Info Portal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #333;
        }
        nav a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            text-align: center;
        }
        nav a:hover {
            background-color: #ddd;
            color: black;
        }
        footer {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        .content {
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to the Student Info Portal</h1>
    </header>
    <nav>
        <a href="#home">Home</a>
        <a href="#profile">Profile</a>
        <a href="#courses">Courses</a>
        <a href="#contact">Contact</a>
    </nav>
    <div class="content">
        <h2>Home</h2>
        <p>This is the homepage of the Student Info Portal. Use the navigation menu to explore.</p>
    </div>
    <footer>
        <p>&copy; 2023 Student Info Portal</p>
    </footer>
</body>
</html>
"""

# Save the HTML content to a file
with open("student_info_portal.html", "w") as file:
    file.write(html_content)

print("HTML homepage has been generated as 'student_info_portal.html'.")