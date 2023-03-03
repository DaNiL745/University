

class Key:
  '''
  Класс для генерации и обращение с ключем.
  Сам ключ представлен как две строки с перемешанным алфавитом
  '''
  ALPHABET_DEFAULT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?.,!'
  ROWS_DEFAULT = 6
  COLS_DEFAULT = 10
  def __init__(self, alphabet=ALPHABET_DEFAULT, rows=ROWS_DEFAULT, cols=COLS_DEFAULT, k0='TORT', k1='CLON'):
    '''
    Принимает на вход символы алфавита и размер таблицы,
    либо использует алфавит по умолчанию
    '''
    def f(l):
        n = []
        for i in l:
            if i not in n:
                n.append(i)
        return n

    self.rows = rows
    self.cols = cols
    self.table=[0]*2

    alph = list(k0) + list(alphabet)
    self.table[0] = f(alph)
    self.table[0] = '|'.join(self.table[0])

    alph = list(k1) + list(alphabet)
    self.table[1] = f(alph)
    self.table[1] = '|'.join(self.table[1])

  def __getitem__(self, key):
    '''
    Если передали кортеж из двух элементов, 
    то это поиск символа в левой (0) или правой (1) таблице
    Если передали кортеж из трех элементов,
    то это получение символа в таблице по координатам
    '''
    if len(key) == 2:
      #table and char
      i = self.table[key[0]].index(key[1])
      return i // self.cols, i % self.cols
    else:
      return self.table[key[0]][key[1]*self.cols+key[2]]

  def __str__(self):
    '''
    Для отображения ключа в читабельном виде
    '''
    s = ''
    for i in range(self.rows):
      s+=self.table[0][i*self.cols:(i+1)*self.cols]+'\t\t'+self.table[1][i*self.cols:(i+1)*self.cols]+'\n'
    return s
  
def bgrams(l):
  '''
  Генератор для разбиения строки на биграммы
  '''
  for i in range(0, len(l), 2):
    yield l[i:i + 2]

def crypt(s, key):
  '''
  Функция шифровки/дешифровки.
  Пробегаемся по всем биграммам и для каждой биграммы
  находим координаты первого символа в первой таблице,
  второго во второй таблице.
  Далее получаем символы из противоположных вершин прямоугольника
  и добавляем к строке с результатом
  '''
  assert len(s) % 2 == 0, 'The string must be divisible by 2'
  r=''
  for bg in bgrams(s):
    (x1, y1), (x2, y2) = key[(0, bg[0])],key[(1, bg[1])]
    r+= key[(0, x2, y1)] + key[(1, x1, y2)]
    #print(bg)
  return r

#Проверка работоспособности
def res(txt, tab0, tab1):
  key = Key(k0=tab0, k1=tab1)
  #print(key)
  s = crypt(txt, key)
  #print(s)
  return s
  #s = crypt(s, key)
  #print(s)
