#ifndef FITNESSLOG_H
#define FITNESSLOG_H

#include <QString>
#include <QVector>

class FitnessLog {
private:
    QString date;
    int steps;
    double sleepHours;
    int calories;

public:
    FitnessLog();
    FitnessLog(QString date, int steps, double sleepHours, int calories);

    QString getDate() const;
    int getSteps() const;
    double getSleepHours() const;
    int getCalories() const;

    static QVector<FitnessLog> readLogsFromCSV(const QString& filename);
};

#endif // FITNESSLOG_H
