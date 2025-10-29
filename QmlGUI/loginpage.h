#ifndef LOGINPAGE_H
#define LOGINPAGE_H

#include <QWidget>

class QLineEdit;
class QPushButton;

class LoginPage : public QWidget
{
    Q_OBJECT
public:
    explicit LoginPage(QWidget *parent = nullptr);

signals:
    void loginSuccess();

private slots:
    void attemptLogin();

private:
    QLineEdit *usernameEdit;
    QLineEdit *passwordEdit;
};

#endif // LOGINPAGE_H
