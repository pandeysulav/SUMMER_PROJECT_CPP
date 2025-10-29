/********************************************************************************
** Form generated from reading UI file 'welcomepage.ui'
**
** Created by: Qt User Interface Compiler version 6.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WELCOMEPAGE_H
#define UI_WELCOMEPAGE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_WelcomePage
{
public:
    QLabel *heartbeatLabel;
    QLabel *exerciseLabel;
    QLabel *logolabel;
    QLabel *signuplabel;
    QLabel *instalabel;
    QLabel *fblabel;
    QLabel *googlelabel;
    QLabel *tiktoklabel;
    QLineEdit *usernameLineEdit;
    QPushButton *loginButton;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout;
    QLabel *label_W;
    QLabel *label_E1;
    QLabel *label_L;
    QLabel *label_C;
    QLabel *label_O;
    QLabel *label_M;
    QLabel *label_E2;

    void setupUi(QWidget *WelcomePage)
    {
        if (WelcomePage->objectName().isEmpty())
            WelcomePage->setObjectName("WelcomePage");
        WelcomePage->resize(1071, 539);
        QSizePolicy sizePolicy(QSizePolicy::Policy::Fixed, QSizePolicy::Policy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(WelcomePage->sizePolicy().hasHeightForWidth());
        WelcomePage->setSizePolicy(sizePolicy);
        WelcomePage->setMinimumSize(QSize(80, 80));
        QFont font;
        font.setFamilies({QString::fromUtf8("MV Boli")});
        font.setPointSize(48);
        WelcomePage->setFont(font);
        WelcomePage->setStyleSheet(QString::fromUtf8("background-color: white"));
        heartbeatLabel = new QLabel(WelcomePage);
        heartbeatLabel->setObjectName("heartbeatLabel");
        heartbeatLabel->setGeometry(QRect(574, 145, 181, 181));
        sizePolicy.setHeightForWidth(heartbeatLabel->sizePolicy().hasHeightForWidth());
        heartbeatLabel->setSizePolicy(sizePolicy);
        heartbeatLabel->setMinimumSize(QSize(70, 70));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Segoe UI")});
        font1.setPointSize(19);
        heartbeatLabel->setFont(font1);
        heartbeatLabel->setPixmap(QPixmap(QString::fromUtf8("images/heartbeat_symbol.png")));
        heartbeatLabel->setScaledContents(true);
        exerciseLabel = new QLabel(WelcomePage);
        exerciseLabel->setObjectName("exerciseLabel");
        exerciseLabel->setGeometry(QRect(753, 88, 251, 171));
        sizePolicy.setHeightForWidth(exerciseLabel->sizePolicy().hasHeightForWidth());
        exerciseLabel->setSizePolicy(sizePolicy);
        exerciseLabel->setMinimumSize(QSize(70, 70));
        exerciseLabel->setPixmap(QPixmap(QString::fromUtf8("images/exercise.png")));
        exerciseLabel->setScaledContents(true);
        logolabel = new QLabel(WelcomePage);
        logolabel->setObjectName("logolabel");
        logolabel->setGeometry(QRect(200, 0, 261, 131));
        sizePolicy.setHeightForWidth(logolabel->sizePolicy().hasHeightForWidth());
        logolabel->setSizePolicy(sizePolicy);
        logolabel->setMinimumSize(QSize(90, 90));
        logolabel->setPixmap(QPixmap(QString::fromUtf8("images/logo.png")));
        logolabel->setScaledContents(true);
        signuplabel = new QLabel(WelcomePage);
        signuplabel->setObjectName("signuplabel");
        signuplabel->setGeometry(QRect(250, 410, 161, 31));
        signuplabel->setMinimumSize(QSize(100, 10));
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Showcard Gothic")});
        font2.setPointSize(15);
        signuplabel->setFont(font2);
        signuplabel->setStyleSheet(QString::fromUtf8("color: #00357b"));
        instalabel = new QLabel(WelcomePage);
        instalabel->setObjectName("instalabel");
        instalabel->setGeometry(QRect(234, 436, 80, 80));
        sizePolicy.setHeightForWidth(instalabel->sizePolicy().hasHeightForWidth());
        instalabel->setSizePolicy(sizePolicy);
        instalabel->setMinimumSize(QSize(80, 80));
        instalabel->setPixmap(QPixmap(QString::fromUtf8("images/insta.png")));
        instalabel->setScaledContents(true);
        fblabel = new QLabel(WelcomePage);
        fblabel->setObjectName("fblabel");
        fblabel->setGeometry(QRect(150, 436, 80, 80));
        sizePolicy.setHeightForWidth(fblabel->sizePolicy().hasHeightForWidth());
        fblabel->setSizePolicy(sizePolicy);
        fblabel->setMinimumSize(QSize(80, 80));
        fblabel->setPixmap(QPixmap(QString::fromUtf8("images/fb.png")));
        fblabel->setScaledContents(true);
        googlelabel = new QLabel(WelcomePage);
        googlelabel->setObjectName("googlelabel");
        googlelabel->setGeometry(QRect(334, 441, 70, 70));
        googlelabel->setMinimumSize(QSize(70, 70));
        googlelabel->setPixmap(QPixmap(QString::fromUtf8("images/google.png")));
        googlelabel->setScaledContents(true);
        tiktoklabel = new QLabel(WelcomePage);
        tiktoklabel->setObjectName("tiktoklabel");
        tiktoklabel->setGeometry(QRect(420, 440, 70, 70));
        sizePolicy.setHeightForWidth(tiktoklabel->sizePolicy().hasHeightForWidth());
        tiktoklabel->setSizePolicy(sizePolicy);
        tiktoklabel->setMinimumSize(QSize(70, 70));
        tiktoklabel->setPixmap(QPixmap(QString::fromUtf8("images/tiktok.png")));
        tiktoklabel->setScaledContents(true);
        usernameLineEdit = new QLineEdit(WelcomePage);
        usernameLineEdit->setObjectName("usernameLineEdit");
        usernameLineEdit->setGeometry(QRect(230, 280, 191, 40));
        usernameLineEdit->setMinimumSize(QSize(100, 40));
        QFont font3;
        font3.setFamilies({QString::fromUtf8("Segoe UI")});
        font3.setPointSize(12);
        usernameLineEdit->setFont(font3);
        usernameLineEdit->setStyleSheet(QString::fromUtf8("color: black"));
        loginButton = new QPushButton(WelcomePage);
        loginButton->setObjectName("loginButton");
        loginButton->setGeometry(QRect(230, 320, 200, 41));
        loginButton->setMinimumSize(QSize(200, 0));
        QFont font4;
        font4.setFamilies({QString::fromUtf8("Showcard Gothic")});
        font4.setPointSize(24);
        loginButton->setFont(font4);
        loginButton->setStyleSheet(QString::fromUtf8("color: #00357b"));
        layoutWidget = new QWidget(WelcomePage);
        layoutWidget->setObjectName("layoutWidget");
        layoutWidget->setGeometry(QRect(11, 140, 585, 112));
        horizontalLayout = new QHBoxLayout(layoutWidget);
        horizontalLayout->setObjectName("horizontalLayout");
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        label_W = new QLabel(layoutWidget);
        label_W->setObjectName("label_W");
        label_W->setMinimumSize(QSize(70, 70));
        label_W->setMaximumSize(QSize(200, 200));
        QFont font5;
        font5.setFamilies({QString::fromUtf8("Showcard Gothic")});
        font5.setPointSize(72);
        label_W->setFont(font5);
        label_W->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_W->setStyleSheet(QString::fromUtf8("color: #00357b"));

        horizontalLayout->addWidget(label_W);

        label_E1 = new QLabel(layoutWidget);
        label_E1->setObjectName("label_E1");
        label_E1->setMinimumSize(QSize(70, 70));
        label_E1->setMaximumSize(QSize(200, 200));
        label_E1->setFont(font5);
        label_E1->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_E1->setStyleSheet(QString::fromUtf8("color: #00357b"));

        horizontalLayout->addWidget(label_E1);

        label_L = new QLabel(layoutWidget);
        label_L->setObjectName("label_L");
        label_L->setMinimumSize(QSize(70, 70));
        label_L->setFont(font5);
        label_L->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_L->setStyleSheet(QString::fromUtf8("color: #00357b"));

        horizontalLayout->addWidget(label_L);

        label_C = new QLabel(layoutWidget);
        label_C->setObjectName("label_C");
        label_C->setMinimumSize(QSize(70, 70));
        label_C->setFont(font5);
        label_C->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_C->setStyleSheet(QString::fromUtf8("color: #00357b"));

        horizontalLayout->addWidget(label_C);

        label_O = new QLabel(layoutWidget);
        label_O->setObjectName("label_O");
        label_O->setMinimumSize(QSize(70, 70));
        label_O->setFont(font5);
        label_O->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_O->setStyleSheet(QString::fromUtf8("color: #00357b"));

        horizontalLayout->addWidget(label_O);

        label_M = new QLabel(layoutWidget);
        label_M->setObjectName("label_M");
        label_M->setMinimumSize(QSize(70, 70));
        label_M->setFont(font5);
        label_M->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_M->setAutoFillBackground(false);
        label_M->setStyleSheet(QString::fromUtf8("color:#00357b"));

        horizontalLayout->addWidget(label_M);

        label_E2 = new QLabel(layoutWidget);
        label_E2->setObjectName("label_E2");
        label_E2->setMinimumSize(QSize(70, 70));
        label_E2->setFont(font5);
        label_E2->setLayoutDirection(Qt::LayoutDirection::LeftToRight);
        label_E2->setStyleSheet(QString::fromUtf8("color: #00357b"));

        horizontalLayout->addWidget(label_E2);


        retranslateUi(WelcomePage);

        QMetaObject::connectSlotsByName(WelcomePage);
    } // setupUi

    void retranslateUi(QWidget *WelcomePage)
    {
        WelcomePage->setWindowTitle(QCoreApplication::translate("WelcomePage", "Form", nullptr));
        heartbeatLabel->setText(QString());
        exerciseLabel->setText(QString());
        logolabel->setText(QString());
        signuplabel->setText(QCoreApplication::translate("WelcomePage", "Sign up with", nullptr));
        instalabel->setText(QString());
        fblabel->setText(QString());
        googlelabel->setText(QString());
        tiktoklabel->setText(QString());
        usernameLineEdit->setPlaceholderText(QCoreApplication::translate("WelcomePage", "Enter Username...", nullptr));
        loginButton->setText(QCoreApplication::translate("WelcomePage", "LOGIN \342\236\234]", nullptr));
#if QT_CONFIG(tooltip)
        label_W->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_W->setText(QCoreApplication::translate("WelcomePage", "W", nullptr));
#if QT_CONFIG(tooltip)
        label_E1->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_E1->setText(QCoreApplication::translate("WelcomePage", "E", nullptr));
#if QT_CONFIG(tooltip)
        label_L->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_L->setText(QCoreApplication::translate("WelcomePage", "L", nullptr));
#if QT_CONFIG(tooltip)
        label_C->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_C->setText(QCoreApplication::translate("WelcomePage", "C", nullptr));
#if QT_CONFIG(tooltip)
        label_O->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_O->setText(QCoreApplication::translate("WelcomePage", "O", nullptr));
#if QT_CONFIG(tooltip)
        label_M->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_M->setText(QCoreApplication::translate("WelcomePage", "M", nullptr));
#if QT_CONFIG(tooltip)
        label_E2->setToolTip(QCoreApplication::translate("WelcomePage", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_E2->setText(QCoreApplication::translate("WelcomePage", "E", nullptr));
    } // retranslateUi

};

namespace Ui {
    class WelcomePage: public Ui_WelcomePage {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WELCOMEPAGE_H
