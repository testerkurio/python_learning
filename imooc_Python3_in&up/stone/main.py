import value
import random

# 计算1颗1级五行石需要多少金
l1_All_value = value.l1_value + value.l1_value_diamond * value.diamond_value

# 计算合成1颗3级需要多少金，= 1级五行石*个数 + 体力 + 合成金
l1_to_l3_OneGold = (l1_All_value * value.l1_to_l3) + (value.l1_to_l3_vit * value.vit_value) + value.l1_to_l3_gold

# 计算合成1颗4级失败的成本
l3_to_l4_Lost = (l1_All_value * value.l3_to_l4) + value.l3_to_l4_gold
print('1颗3级合成4级时失败成本：',l3_to_l4_Lost)

# 计算合成1颗4级需要多少金，= 3级五行石 + 1级五行石*个数 + 体力 + 合成金
l3_to_l4_OneGold = l1_to_l3_OneGold + (l1_All_value * value.l3_to_l4) + (value.l3_to_l4_vit * value.vit_value) + value.l3_to_l4_gold

# 计算12颗4级合成所需要的成本（成功几率随机）
l4_Allgold = 0
for i in range(0,12):
	l4_Allgold += l3_to_l4_OneGold + (l3_to_l4_Lost * random.randint(0,1))

# 计算合成1颗6级需要多少金，= 4级五行石*个数 + 体力 + 合成金
l4_to_l6_OneGold = l4_Allgold + (value.l4_to_l6_vit * value.vit_value) + value.l4_to_l6_gold

l4_to_l6_MinGold = (l3_to_l4_OneGold * value.l4_to_l6) + (value.l4_to_l6_vit * value.vit_value) + value.l4_to_l6_gold

l4_to_l6_MaxGold = ((l3_to_l4_OneGold + l3_to_l4_Lost) * value.l4_to_l6) + (value.l4_to_l6_vit * value.vit_value) + value.l4_to_l6_gold

print('随机成功概率下的6级五行石合成成本: ',l4_to_l6_OneGold)
print('最好运气全部成功的6级五行石合成成本：',l4_to_l6_MinGold)
print('每次合成4级需要合成2次的6级五行石合成成本：',l4_to_l6_MaxGold)