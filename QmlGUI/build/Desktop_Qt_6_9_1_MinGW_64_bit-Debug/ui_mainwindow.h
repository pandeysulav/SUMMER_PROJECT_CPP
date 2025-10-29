/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout;
    QWidget *sidebarWidget;
    QPushButton *homeButton;
    QPushButton *summaryButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QWidget *layoutWidget1;
    QHBoxLayout *horizontalLayout;
    QStackedWidget *stackedWidget;
    QWidget *homePage;
    QLabel *label_2;
    QLabel *label;
    QLabel *label_6;
    QLabel *label_7;
    QWidget *summaryPage;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_8;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(941, 548);
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: white"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        layoutWidget = new QWidget(centralwidget);
        layoutWidget->setObjectName("layoutWidget");
        layoutWidget->setGeometry(QRect(-10, -20, 102, 571));
        verticalLayout = new QVBoxLayout(layoutWidget);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        sidebarWidget = new QWidget(layoutWidget);
        sidebarWidget->setObjectName("sidebarWidget");
        sidebarWidget->setMinimumSize(QSize(100, 150));
        sidebarWidget->setStyleSheet(QString::fromUtf8("background-color: #00357b"));
        homeButton = new QPushButton(sidebarWidget);
        homeButton->setObjectName("homeButton");
        homeButton->setGeometry(QRect(-30, 30, 162, 158));
        QIcon icon;
        icon.addFile(QString::fromUtf8("images/home.png"), QSize(), QIcon::Mode::Normal, QIcon::State::Off);
        homeButton->setIcon(icon);
        homeButton->setIconSize(QSize(150, 150));
        homeButton->setFlat(true);
        summaryButton = new QPushButton(sidebarWidget);
        summaryButton->setObjectName("summaryButton");
        summaryButton->setGeometry(QRect(-30, 290, 172, 168));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8("images/summary.png"), QSize(), QIcon::Mode::Normal, QIcon::State::Off);
        summaryButton->setIcon(icon1);
        summaryButton->setIconSize(QSize(160, 160));
        summaryButton->setFlat(true);
        pushButton_2 = new QPushButton(sidebarWidget);
        pushButton_2->setObjectName("pushButton_2");
        pushButton_2->setGeometry(QRect(10, 170, 91, 131));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8("images/notification.png"), QSize(), QIcon::Mode::Normal, QIcon::State::Off);
        pushButton_2->setIcon(icon2);
        pushButton_2->setIconSize(QSize(160, 160));
        pushButton_2->setFlat(true);
        pushButton_3 = new QPushButton(sidebarWidget);
        pushButton_3->setObjectName("pushButton_3");
        pushButton_3->setGeometry(QRect(0, 440, 111, 111));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8("images/settings.png"), QSize(), QIcon::Mode::Normal, QIcon::State::Off);
        pushButton_3->setIcon(icon3);
        pushButton_3->setIconSize(QSize(160, 160));
        pushButton_3->setFlat(true);

        verticalLayout->addWidget(sidebarWidget);

        layoutWidget1 = new QWidget(centralwidget);
        layoutWidget1->setObjectName("layoutWidget1");
        layoutWidget1->setGeometry(QRect(90, 0, 981, 551));
        horizontalLayout = new QHBoxLayout(layoutWidget1);
        horizontalLayout->setObjectName("horizontalLayout");
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        stackedWidget = new QStackedWidget(layoutWidget1);
        stackedWidget->setObjectName("stackedWidget");
        stackedWidget->setStyleSheet(QString::fromUtf8("background-color: white"));
        homePage = new QWidget();
        homePage->setObjectName("homePage");
        label_2 = new QLabel(homePage);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(310, 110, 49, 16));
        label = new QLabel(homePage);
        label->setObjectName("label");
        label->setGeometry(QRect(0, 0, 971, 541));
        label->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/user1.png")));
        label->setScaledContents(true);
        label_6 = new QLabel(homePage);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(330, 160, 49, 16));
        label_7 = new QLabel(homePage);
        label_7->setObjectName("label_7");
        label_7->setGeometry(QRect(0, 0, 821, 551));
        QSizePolicy sizePolicy(QSizePolicy::Policy::Fixed, QSizePolicy::Policy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_7->sizePolicy().hasHeightForWidth());
        label_7->setSizePolicy(sizePolicy);
        label_7->setAutoFillBackground(false);
        label_7->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/2.jpg")));
        label_7->setScaledContents(true);
        stackedWidget->addWidget(homePage);
        summaryPage = new QWidget();
        summaryPage->setObjectName("summaryPage");
        label_3 = new QLabel(summaryPage);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(0, 0, 981, 541));
        sizePolicy.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy);
        label_3->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/gg.png")));
        label_3->setScaledContents(true);
        label_4 = new QLabel(summaryPage);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(30, 80, 411, 271));
        sizePolicy.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
        label_4->setSizePolicy(sizePolicy);
        label_4->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/user1_good_fitness_plot.png")));
        label_4->setScaledContents(true);
        label_5 = new QLabel(summaryPage);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(470, 90, 361, 261));
        sizePolicy.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy);
        label_5->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/user1_fitness_comparison.png")));
        label_5->setScaledContents(true);
        label_8 = new QLabel(summaryPage);
        label_8->setObjectName("label_8");
        label_8->setGeometry(QRect(0, 0, 851, 551));
        sizePolicy.setHeightForWidth(label_8->sizePolicy().hasHeightForWidth());
        label_8->setSizePolicy(sizePolicy);
        label_8->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/3.jpg")));
        label_8->setScaledContents(true);
        stackedWidget->addWidget(summaryPage);

        horizontalLayout->addWidget(stackedWidget);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        stackedWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        homeButton->setText(QString());
        summaryButton->setText(QString());
        pushButton_2->setText(QString());
        pushButton_3->setText(QString());
        label_2->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label->setText(QString());
        label_6->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        label_7->setText(QString());
        label_3->setText(QString());
        label_4->setText(QString());
        label_5->setText(QString());
        label_8->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
