# Author: OakAnderson(andersonfelipe01@live.com)
# Author: ZauJulio(zauhdf@gmail.com)
#
# Present...
# 
# 


class Mamao:
    def __init__(self, pitaya):
        """  """
        if isinstance(pitaya, dict):
            self.__dict__ = pitaya
            for item in pitaya.keys():
                self.__dict__[item] = self._reconstructor(self.__dict__[item])

    def _reconstructor(self, carambola):
        """  """
        if isinstance(carambola, dict):
            return Mamao(carambola)

        return carambola
