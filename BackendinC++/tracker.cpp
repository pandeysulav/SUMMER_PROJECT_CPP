#include "tracker.h"

void Tracker::setUser(const User& u) {
    user = u;
}

void Tracker::addLog(const FitnessLog& log) {
    logs.append(log);
}

QVector<FitnessLog> Tracker::getLogs() const {
    return logs;
}

User Tracker::getUser() const {
    return user;
}
