from Mathematique import Somme ,Maximum ,Moyenne , puissance
import pytest
def test_somme():
    assert Somme(12,0)==12
    assert Somme(-3,-6)==-9
    assert Somme(0,0)==0
    assert Somme(-1,1)==0
def test_max():
    assert   Maximum(12,0)==12 
    assert Maximum(0,12)==12
    assert Maximum(0,0)==0
    assert Maximum(-1,-10)==-1
def test_moy():
    assert Moyenne(5,7)==6
    assert Moyenne(3,-5)==-1
    assert Moyenne(0,0)==0
    
def test_puiss():
    assert    puissance(0,0)==1
    assert puissance(2,-3)==0.125
    assert puissance(2,3)==8
    assert puissance(-2,-3)==-0.125
    with pytest.raises(ValueError , match="entrée non valide"):
        puissance(0,-3)  