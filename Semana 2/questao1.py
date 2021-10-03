# Retorne a posição de todos os números de um determinado array,
# entre 5 e 10. Array de exemplo: [2, 6, 1, 9, 10, 3, 27]

a = np.array([2,6,1,9,10,3,27])
id1 = np.where(np.logical_and(a>5, a<10))
print(id1[0])