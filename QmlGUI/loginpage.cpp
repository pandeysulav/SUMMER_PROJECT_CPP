#include "loginpage.h"
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include <QLabel>
#include <QMessageBox>

LoginPage::LoginPage(QWidget *parent) : QWidget(parent)
{
    QVBoxLayout *layout = new QVBoxLayout(this);

    usernameEdit = new QLineEdit();
    usernameEdit->setPlaceholderText("Username");
    layout->addWidget(usernameEdit);

    passwordEdit = new QLineEdit();
    passwordEdit->setPlaceholderText("Password");
    passwordEdit->setEchoMode(QLineEdit::Password);
    layout->addWidget(passwordEdit);

    QPushButton *loginButton = new QPushButton("Login");
    layout->addWidget(loginButton);

    connect(loginButton, &QPushButton::clicked, this, &LoginPage::attemptLogin);
}

void LoginPage::attemptLogin()
{
    QString username = usernameEdit->text();
    QString password = passwordEdit->text();

    if ((username == "User1" && password == "1234") ||
        (username == "User4" && password == "abcd"))
    {
        emit loginSuccess();
    }
    else
    {
        QMessageBox::warning(this, "Login Failed", "Invalid username or password");
    }
}
