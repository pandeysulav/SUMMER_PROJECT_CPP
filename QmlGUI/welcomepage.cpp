#include "welcomepage.h"
#include "ui_welcomepage.h"

#include <QPropertyAnimation>
#include <QSequentialAnimationGroup>
#include <QEasingCurve>
#include <QMessageBox>
#include <QTimer>
#include <QPauseAnimation>

WelcomePage::WelcomePage(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::WelcomePage)
{
    ui->setupUi(this);

    // Start welcome text animation shortly after the window is shown
    QTimer::singleShot(100, this, &WelcomePage::startWelcomeAnimation);
}

WelcomePage::~WelcomePage()
{
    delete ui;
}

void WelcomePage::startWelcomeAnimation()
{
    QSequentialAnimationGroup *group = new QSequentialAnimationGroup(this);

    QList<QLabel*> letters = {
        ui->label_W,
        ui->label_E1,
        ui->label_L,
        ui->label_C,
        ui->label_O,
        ui->label_M,
        ui->label_E2
    };

    // Hide all letters initially
    for (QLabel* letter : letters) {
        letter->hide();
    }

    for (int i = 0; i < letters.size(); ++i) {
        QLabel* letter = letters[i];

        QPoint finalPos = letter->pos();

        // Move letter offscreen left before showing it
        letter->move(finalPos.x() - 100, finalPos.y());

        // Show the letter now (it's offscreen so invisible)
        letter->show();

        QPropertyAnimation *anim = new QPropertyAnimation(letter, "pos");
        anim->setDuration(400);
        anim->setStartValue(QPoint(finalPos.x() - 100, finalPos.y()));
        anim->setEndValue(finalPos);
        anim->setEasingCurve(QEasingCurve::OutCubic);

        group->addAnimation(anim);

        if (i != letters.size() - 1) {
            QPauseAnimation* pause = new QPauseAnimation(150, group);
            group->addAnimation(pause);
        }
    }

    group->start(QAbstractAnimation::DeleteWhenStopped);
}

void WelcomePage::on_loginButton_clicked()
{
    QString username = ui->usernameLineEdit->text();

    if (username == "User1" || username == "User4") {
        emit loginSuccessful();
    } else {
        QMessageBox::warning(this, "Login Failed", "Invalid username. Try again.");
    }
}
