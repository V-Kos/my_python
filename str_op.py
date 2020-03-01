{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = \"У лукоморья 123 дуб зеленый 456\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Данная буква на 10 позиции\n"
     ]
    }
   ],
   "source": [
    "\n",
    "ind=s.find(\"я\")\n",
    "if ind == -1:\n",
    "    print(\"Данной буквы нет\")\n",
    "else:\n",
    "    print(\"Данная буква на\",ind,\"позиции\" )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Данная буква встречается 2 раз\n"
     ]
    }
   ],
   "source": [
    "lc=s.count(\"у\")\n",
    "print(\"Данная буква встречается\",lc,\"раз\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "У ЛУКОМОРЬЯ 123 ДУБ ЗЕЛЕНЫЙ 456\n"
     ]
    }
   ],
   "source": [
    "if s.isalpha():\n",
    "    print(\"Да,состоит\")\n",
    "else:\n",
    "    print(s.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "у лукоморья 123 дуб зеленый 456\n"
     ]
    }
   ],
   "source": [
    "l=len(s)\n",
    "if l< 4:\n",
    "    print(\"Данная строка состоит меньше чем из 4 элементов\")\n",
    "else:\n",
    "    print(s.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "O лукоморья 123 дуб зеленый 456\n"
     ]
    }
   ],
   "source": [
    "print(s.replace(s[0],\"O\"))"
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
