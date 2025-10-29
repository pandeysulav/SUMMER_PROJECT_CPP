#include <QApplication>
#include "welcomepage.h"
#include "mainwindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    WelcomePage welcome;
    MainWindow mainWindow;

    // Connect the loginSuccessful signal from WelcomePage to show MainWindow
    QObject::connect(&welcome, &WelcomePage::loginSuccessful, [&]() {
        welcome.hide();
        mainWindow.show();
    });

    welcome.show();

    return a.exec();
}
