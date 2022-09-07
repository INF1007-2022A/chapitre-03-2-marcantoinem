#!/usr/bin/env python

import math

def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage ** 2 / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	produit_scalaire = 0
	for x,y in v1, v2:
		produit_scalaire += x*y
	return produit_scalaire == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	nb_value = 0
	somme = 0
	for v in values:
		if v >= 0:
			somme += v
			nb_value += 1
	return somme / nb_value

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = value // 20
	rest = value - 20*twenties
	tens = rest // 10
	rest -= 10 * tens
	fives = rest // 5
	rest -= 5 * fives
	twos = rest // 2
	rest -= 2*twos
	ones = rest
	return (twenties, tens, fives, twos, ones)

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donnée en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	max_digit = math.floor(math.log(abs_value, base))
	for i in range(max_digit, -1, -1):
		print(i)
		character = abs_value // (base ** i)
		result += digit_letters[character]
		abs_value -= character * (base ** i)
	if value < 0:
		result = "-" + result
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
