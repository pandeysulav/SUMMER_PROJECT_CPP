#include "AppController.h"

AppController::AppController(QObject *parent)
    : QObject(parent)
{
}

QString AppController::activeUser() const
{
    return m_activeUser;
}

void AppController::login(const QString &username)
{
    if (username == "User1" || username == "User4") {
        m_activeUser = username;
        emit activeUserChanged();
        emit showHomePage();  // Triggers navigation to HomePage in QML
    } else {
        qWarning("Invalid user. Only 'User1' and 'User4' are allowed.");
    }
}

void AppController::goToHome()
{
    emit showHomePage();
}

void AppController::goToSummary()
{
    emit showSummaryPage();
}
