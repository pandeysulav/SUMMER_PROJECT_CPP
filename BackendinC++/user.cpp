#include "user.h"

User::User() {}

User::User(QString name, int age, double weight, double height)
    : name(name), age(age), weight(weight), height(height) {}

double User::getBMI() const {
    return weight / ((height / 100) * (height / 100));  // cm to meters
}

QString User::getName() const { return name; }
int User::getAge() const { return age; }
double User::getWeight() const { return weight; }
double User::getHeight() const { return height; }
