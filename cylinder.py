#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program calculates the volume of a cylinder


import math

def calculate_volume(radius, height):
    # calculate volume

    # process
    volume = math.pi * (radius**2) * height

    # output
    return volume


def main():
    # this function gets the user input

    # input
    radius_as_string = input("The radius of a cylinder is (cm) : ")
    height_as_string = input("The height of a cylinder is (cm) : ")
    # call function
    try:
        radius_from_user = float(radius_as_string)
        height_from_user = float(height_as_string)
        calculated_volume = round (calculate_volume(radius_from_user, height_from_user), 2)
        print("\nThe volume of a cylinder with {0} cm radius and {1} cm height is {2} cm³.".format(radius_from_user, height_from_user, calculated_volume))
    except Exception:
        print("\nInvalid integer entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
