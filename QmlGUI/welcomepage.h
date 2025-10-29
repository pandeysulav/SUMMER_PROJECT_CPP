#ifndef WELCOMEPAGE_H
#define WELCOMEPAGE_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class WelcomePage; }
QT_END_NAMESPACE

class WelcomePage : public QMainWindow
{
    Q_OBJECT

public:
    explicit WelcomePage(QWidget *parent = nullptr);
    ~WelcomePage();

signals:
    void loginSuccessful();  // <-- Declare the signal here

private slots:
    void startWelcomeAnimation();
    void on_loginButton_clicked();

private:
    Ui::WelcomePage *ui;
};

#endif // WELCOMEPAGE_H
