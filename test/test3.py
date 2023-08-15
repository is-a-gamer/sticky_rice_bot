import json

all_data = {
    "data": {
        "hideoutStations": [
            {
                "name": "加热器",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 25000
                            },
                            {
                                "item": {
                                    "name": "经典火柴"
                                },
                                "count": 2
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 50000
                            },
                            {
                                "item": {
                                    "name": "Hunter火柴"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "固体燃料"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "Crickent打火机"
                                },
                                "count": 3
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "螺旋散热器"
                                },
                                "count": 8
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 8
                            },
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "军用波纹软管"
                                },
                                "count": 2
                            }
                        ]
                    }
                ]
            },
            {
                "name": "发电机",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 100000
                            },
                            {
                                "item": {
                                    "name": "火花塞"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "Bulbex剪线器"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "火花塞"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "供电单元"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 7
                            }
                        ]
                    }
                ]
            },
            {
                "name": "通风",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 25000
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "汽车蓄电池"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "CPU风扇"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 2
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 14
                            },
                            {
                                "item": {
                                    "name": "印制电路板"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "汽车蓄电池"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 5
                            }
                        ]
                    }
                ]
            },
            {
                "name": "安保",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 20000
                            },
                            {
                                "item": {
                                    "name": "施工用测量卷尺"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 45000
                            },
                            {
                                "item": {
                                    "name": "Elite钳子"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "100毫升WD-40"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "TP-200 砖型TNT"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "可用液晶显示屏"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "NIXXOR镜头"
                                },
                                "count": 8
                            },
                            {
                                "item": {
                                    "name": "固态硬盘"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "卫生间",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 2000
                            },
                            {
                                "item": {
                                    "name": "卫生纸"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "牙膏"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "肥皂"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "缝纫锥"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "一包螺钉"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "KEKTAPE管道胶带"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "针线盒"
                                },
                                "count": 2
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "压力表"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "Xenomorph发泡密封胶"
                                },
                                "count": 3
                            }
                        ]
                    }
                ]
            },
            {
                "name": "仓库",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": []
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "手摇钻"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "一包螺钉"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "100毫升WD-40"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 2500000
                            },
                            {
                                "item": {
                                    "name": "一包钉子"
                                },
                                "count": 5
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "一包螺钉"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 8500000
                            },
                            {
                                "item": {
                                    "name": "一包钉子"
                                },
                                "count": 7
                            }
                        ]
                    },
                    {
                        "level": 4,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "欧元"
                                },
                                "count": 200000
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "螺母"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "Shustrilo发泡密封胶"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "棘轮扳手"
                                },
                                "count": 2
                            }
                        ]
                    }
                ]
            },
            {
                "name": "集水器",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "螺母"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "管道胶带"
                                },
                                "count": 3
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "KEKTAPE管道胶带"
                                },
                                "count": 2
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 20000
                            },
                            {
                                "item": {
                                    "name": "Elite钳子"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "Shustrilo发泡密封胶"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "棘轮扳手"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "医疗站",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 50000
                            },
                            {
                                "item": {
                                    "name": "一次性注射器"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "一堆药"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "无菌绷带"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "OLOLO瓶装复合维生素"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 150000
                            },
                            {
                                "item": {
                                    "name": "医用输血工具"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "盐水溶液"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "Esmarch止血带"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "医疗工具"
                                },
                                "count": 3
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 500000
                            },
                            {
                                "item": {
                                    "name": "盐水溶液"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "LEDX皮肤透照仪"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "检眼镜"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "营养部",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 25000
                            },
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "电源线"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "罐装白盐"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "扳手"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "碱性换热器表面洗涤剂"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 125000
                            },
                            {
                                "item": {
                                    "name": "Majaica咖啡"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "碳酸氢钠"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "Smoked Chimney下水道清洁剂"
                                },
                                "count": 2
                            }
                        ]
                    }
                ]
            },
            {
                "name": "休息区",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 10000
                            },
                            {
                                "item": {
                                    "name": "管道胶带"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "经典火柴"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 35000
                            },
                            {
                                "item": {
                                    "name": "DVD光驱"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电磁铁"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "节能灯泡"
                                },
                                "count": 3
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电源线"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "电容"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 7
                            },
                            {
                                "item": {
                                    "name": "GreenBat锂电池"
                                },
                                "count": 5
                            }
                        ]
                    }
                ]
            },
            {
                "name": "情报中心",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "情报文件夹"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "地形调查地图"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "工厂地图"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "情报文件夹"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "加密U盘"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "电源线"
                                },
                                "count": 7
                            },
                            {
                                "item": {
                                    "name": "损坏的硬盘"
                                },
                                "count": 4
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "军用COFDM无线信号发射器"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "VPX闪存模块"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "军用闪存装置"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "军用电缆"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "加密磁带盒"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "GPS信号放大单元"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "图书馆",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 400000
                            },
                            {
                                "item": {
                                    "name": "马雕像"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "项链"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "技术指导文件"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "日记"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "袖珍日记"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "BakeEzy烹饪书"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Scav宝箱",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "青铜狮雕"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "黄金骷髅指环"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "金项链"
                                },
                                "count": 8
                            },
                            {
                                "item": {
                                    "name": "劳力土潜水金腕表"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "“凶狠跑刀崽”月光"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "幸运Scav垃圾箱"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "金公鸡"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "照明",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 10000
                            },
                            {
                                "item": {
                                    "name": "Crickent打火机"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电灯泡"
                                },
                                "count": 14
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 10
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 50000
                            },
                            {
                                "item": {
                                    "name": "电容"
                                },
                                "count": 7
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "节能灯泡"
                                },
                                "count": 12
                            }
                        ]
                    }
                ]
            },
            {
                "name": "空气过滤单元",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "美元"
                                },
                                "count": 25000
                            },
                            {
                                "item": {
                                    "name": "军用电源滤波器"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "防毒面具滤罐"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "军用波纹软管"
                                },
                                "count": 3
                            }
                        ]
                    }
                ]
            },
            {
                "name": "太阳能",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "欧元"
                                },
                                "count": 25000
                            },
                            {
                                "item": {
                                    "name": "军用电缆"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "相控阵单元"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "军用电源滤波器"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "可用液晶显示屏"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "直流变压器"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "酒饮生成器",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "硅胶管"
                                },
                                "count": 4
                            },
                            {
                                "item": {
                                    "name": "模拟温度计"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "压力表"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "管道扳手"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "螺旋散热器"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 2
                            }
                        ]
                    }
                ]
            },
            {
                "name": "比特币矿场",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "CPU风扇"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "供电单元"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "电源线"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "VPX闪存模块"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "T形插座"
                                },
                                "count": 5
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "CPU风扇"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "供电单元"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "印制电路板"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "军用电源滤波器"
                                },
                                "count": 2
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "CPU风扇"
                                },
                                "count": 25
                            },
                            {
                                "item": {
                                    "name": "硅胶管"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "压力表"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "6-STEN-140-M军用电池"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "工作台",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "螺母"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "Leatherman多功能工具钳"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "武器零件"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "\"Master\"锉刀套装"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 395000
                            },
                            {
                                "item": {
                                    "name": "Elite钳子"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "#FireKlean牌枪润滑油"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "罐装铝热剂"
                                },
                                "count": 2
                            }
                        ]
                    }
                ]
            },
            {
                "name": "射击场",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "螺母"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "卢布"
                                },
                                "count": 20000
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "施工用测量卷尺"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "一包螺钉"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "Poxeram冷焊膏"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电动马达"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "节能灯泡"
                                },
                                "count": 6
                            },
                            {
                                "item": {
                                    "name": "WIFI摄像头"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "\"Master\"锉刀套装"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "印制电路板"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "电容"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "相位控制继电器"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "电源线"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "Leatherman多功能工具钳"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "技术指导文件"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "健身区",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "金属切割剪刀"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "螺母"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "100毫升WD-40"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "绝缘胶带"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            },
            {
                "name": "易碎墙",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": []
                    },
                    {
                        "level": 2,
                        "itemRequirements": []
                    },
                    {
                        "level": 3,
                        "itemRequirements": []
                    },
                    {
                        "level": 4,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "Fierce Blow重击锤"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 5,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "金属切割剪刀"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 1
                            }
                        ]
                    },
                    {
                        "level": 6,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "波纹软管"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "管道胶带"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "一套工具"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "Elite钳子"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "Xenomorph发泡密封胶"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 2
                            },
                            {
                                "item": {
                                    "name": "电灯泡"
                                },
                                "count": 2
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Weapon Stand",
                "levels": [
                    {
                        "level": 1,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "手摇钻"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "金属切割剪刀"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "节能灯泡"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "Xenomorph发泡密封胶"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "螺栓"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "绝缘胶带"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "一包钉子"
                                },
                                "count": 5
                            }
                        ]
                    },
                    {
                        "level": 2,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "\"Master\"锉刀套装"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "节能灯泡"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "一包螺钉"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "管道胶带"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "武器零件"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "Poxeram冷焊膏"
                                },
                                "count": 3
                            }
                        ]
                    },
                    {
                        "level": 3,
                        "itemRequirements": [
                            {
                                "item": {
                                    "name": "电钻"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "节能灯泡"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "金属零件"
                                },
                                "count": 10
                            },
                            {
                                "item": {
                                    "name": "KEKTAPE管道胶带"
                                },
                                "count": 5
                            },
                            {
                                "item": {
                                    "name": "电线"
                                },
                                "count": 15
                            },
                            {
                                "item": {
                                    "name": "Shustrilo发泡密封胶"
                                },
                                "count": 3
                            },
                            {
                                "item": {
                                    "name": "技术指导文件"
                                },
                                "count": 1
                            },
                            {
                                "item": {
                                    "name": "#FireKlean牌枪润滑油"
                                },
                                "count": 1
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

item_req = {}

for ca in all_data["data"]["hideoutStations"]:
    if ca["name"] == "仓库":
        continue

    for l in ca["levels"]:
        for i in l["itemRequirements"]:
            if i["item"]["name"] in item_req:
                item_req[i["item"]["name"]] += i["count"]
            else:
                item_req[i["item"]["name"]] = i["count"]

print(item_req)
