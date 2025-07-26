#ifndef TRACKER_H
#define TRACKER_H

#include "user.h"
#include "fitnesslog.h"
#include <QVector>

class Tracker {
private:
    User user;
    QVector<FitnessLog> logs;

public:
    void setUser(const User& u);
    void addLog(const FitnessLog& log);
    QVector<FitnessLog> getLogs() const;
    User getUser() const;
};

#endif
