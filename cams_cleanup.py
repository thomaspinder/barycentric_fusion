import iris

if __name__=='__main__':
    cube = iris.load("data/cams_pm25_2016.nc")
    print(cube)
    

