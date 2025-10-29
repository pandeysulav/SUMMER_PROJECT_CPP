#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMovie>
#include <QLabel>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Connect sidebar buttons to page switch slots
    connect(ui->homeButton, &QPushButton::clicked, this, &MainWindow::showHomePage);
    connect(ui->summaryButton, &QPushButton::clicked, this, &MainWindow::showSummaryPage);


    // Optional: center align the label
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::showHomePage()
{
    // Replace 'stackedWidget' with the actual object name of your QStackedWidget in the UI
    ui->stackedWidget->setCurrentWidget(ui->homePage);
}

void MainWindow::showSummaryPage()
{
    ui->stackedWidget->setCurrentWidget(ui->summaryPage);
}
