/********************************************************************************
** Form generated from reading UI file 'loginpage.ui'
**
** Created by: Qt User Interface Compiler version 6.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINPAGE_H
#define UI_LOGINPAGE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_loginpage
{
public:

    void setupUi(QWidget *loginpage)
    {
        if (loginpage->objectName().isEmpty())
            loginpage->setObjectName("loginpage");
        loginpage->resize(400, 300);

        retranslateUi(loginpage);

        QMetaObject::connectSlotsByName(loginpage);
    } // setupUi

    void retranslateUi(QWidget *loginpage)
    {
        loginpage->setWindowTitle(QCoreApplication::translate("loginpage", "Form", nullptr));
    } // retranslateUi

};

namespace Ui {
    class loginpage: public Ui_loginpage {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINPAGE_H
