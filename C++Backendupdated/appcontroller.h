#ifndef APPCONTROLLER_H
#define APPCONTROLLER_H

#include <QObject>

class AppController : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString activeUser READ activeUser NOTIFY activeUserChanged)

public:
    explicit AppController(QObject *parent = nullptr);

    QString activeUser() const;

    Q_INVOKABLE void login(const QString &username);
    Q_INVOKABLE void goToHome();
    Q_INVOKABLE void goToSummary();

signals:
    void activeUserChanged();
    void showHomePage();
    void showSummaryPage();

private:
    QString m_activeUser;
};

#endif // APPCONTROLLER_H
