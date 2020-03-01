{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ле?о\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Введите недостоющую букву т\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Победа! \n",
      " т\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "l=[\"самовар\",\"весна\",\"лето\"]\n",
    "randomW = random.choice(l)\n",
    "randomL = random.choice(randomW)\n",
    "l2 = randomW.split(randomL)\n",
    "print(\"?\".join(l2))\n",
    "if input(\"Введите недостоющую букву\")==randomL:\n",
    "    print(\"Победа!\",'\\n',randomL)\n",
    "else:\n",
    "    print(\"Увы! Попробуйте в другой раз.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
