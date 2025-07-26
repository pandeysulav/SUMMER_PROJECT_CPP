#include "fitnesslog.h"
#include <QFile>
#include <QTextStream>
#include <QDebug>

FitnessLog::FitnessLog() {}

FitnessLog::FitnessLog(QString date, int steps, double sleepHours, int calories)
    : date(date), steps(steps), sleepHours(sleepHours), calories(calories) {}

QString FitnessLog::getDate() const { return date; }
int FitnessLog::getSteps() const { return steps; }
double FitnessLog::getSleepHours() const { return sleepHours; }
int FitnessLog::getCalories() const { return calories; }

QVector<FitnessLog> FitnessLog::readLogsFromCSV(const QString& filename) {
    QVector<FitnessLog> logs;

    QFile file(filename);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "Failed to open file";
        return logs;
    }

    QTextStream in(&file);
    while (!in.atEnd()) {
        QString line = in.readLine();
        QStringList parts = line.split(',');

        if (parts.size() == 4) {
            QString date = parts[0];
            int steps = parts[1].toInt();
            double sleepHours = parts[2].toDouble();
            int calories = parts[3].toInt();

            logs.append(FitnessLog(date, steps, sleepHours, calories));
        }
    }

    file.close();
    return logs;
}
