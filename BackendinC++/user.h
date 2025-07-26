#ifndef USER_H
#define USER_H

#include <QString>

class User {
private:
    QString name;
    int age;
    double weight;
    double height;

public:
    User();
    User(QString name, int age, double weight, double height);

    double getBMI() const;
    QString getName() const;
    int getAge() const;
    double getWeight() const;
    double getHeight() const;
};

#endif
