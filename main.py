print('—— ' * 30)
print('\t' * 9, '交通罚单管理系统\n')
print('\t' * 7, ' 1.录入罚单信息', '\t', '4.查询罚单信息')
print('\t' * 7, ' 2.删除罚单信息', '\t', '5.查看未缴罚单')
print('\t' * 7, ' 3.修改罚单信息', '\t', '6.查看所有罚单')
print('\t' * 7, ' 0.退出系统\n')
print('—— ' * 30)

class Ticket():
    def __init__(self, ticket_id, driver_name, driver_id, driver_level, driver_phone, car_num, car_type, action, statu):
        self.ticket_id = ticket_id # 罚单编号
        self.driver_name = driver_name # 被处罚人姓名
        self.driver_id = driver_id # 被处罚人身份证号
        self.driver_level = driver_level # 被处罚人驾照等级
        self.driver_phone = driver_phone # 被处罚人手机号
        self.car_num = car_num # 车辆牌号
        self.car_type = car_type # 车辆类型
        self.action = action # 违法行为
        self.statu = statu # 罚单缴纳情况

    def __repr__(self):
        return f"{self.ticket_id} | {self.driver_name} | {self.driver_id} | {self.driver_level} | {self.driver_phone} | {self.car_num} | {self.car_type} | {self.action} | {self.statu}"


class Ticket_exec:
    def __init__(self):
        self.ticket_list = [
            Ticket('1', '张三', '210200200101010101', 'C1', '19966991111', '辽A 11111', '轿车', '违停', '0'),
            Ticket('2', '李四', '210200200202020202', 'C2', '19966992222', '辽B 22222', '轿车', '超速', '0'),
            Ticket('3', '王五', '210200200303030303', 'B1', '19966993333', '辽C 33333', '小型货车', '闯红灯', '0'),
        ]

    def create_ticket(self):
        print('--------录入罚单信息--------')
        ticket_id = str(len(self.ticket_list) + 1)
        driver_name = input('被处罚人姓名:')
        driver_id = input('被处罚人身份证号:')
        driver_level = input('被处罚人驾照等级:')
        driver_phone = input('被处罚人手机号:')
        car_num = input('车辆牌号:')
        car_type = input('车辆类型:')
        action = input('违法行为:')
        statu = '0'

        ticket_new = Ticket(ticket_id, driver_name, driver_id, driver_level, driver_phone, car_num, car_type, action, statu)
        self.ticket_list.append(ticket_new)
        print(f'录入罚单:\n{ticket_new}\n')
        return

    def delete_ticket(self):
        print('--------删除罚单信息--------')
        self.show_all_ticket()
        ticket_id = input('请输入罚单编号删除:')
        for ticket in self.ticket_list:
            if ticket_id == ticket.ticket_id:
                check = input('确认删除?(Y/N):')
                if check == 'Y' or check == 'y':
                    self.ticket_list.remove(ticket)
                    print('罚单删除成功!')
                else:
                    print('取消删除!')
                return
        print('该罚单编号不存在!')
        return

    def update_ticket(self):
        print('--------修改罚单信息--------')
        ticket_id = input('请输入罚单编号修改:')
        for ticket in self.ticket_list:
            if ticket_id == ticket.ticket_id:
                print(f'查询到如下信息:\n{ticket}\n')
                ticket.driver_name = input('请输入被处罚人姓名:')
                ticket.driver_id = input('请输入被处罚人身份证号:')
                ticket.driver_level = input('请输入被处罚人驾照等级:')
                ticket.driver_phone = input('请输入被处罚人手机号:')
                ticket.car_num = input('请输入车辆牌号:')
                ticket.car_type = input('请输入车辆类型:')
                ticket.action = input('请输入违法行为:')
                ticket.statu = input('请输入罚单缴纳情况:')
                print(f'罚单信息已修改为:\n{ticket}\n')
                return
        print('该罚单编号不存在!')
        return

    def select_ticket(self):
        print('--------查询罚单信息--------')
        ticket_id = input('请输入罚单编号:')
        for ticket in self.ticket_list:
            if ticket_id == ticket.ticket_id:
                print(f'查询到如下信息:\n{ticket}\n')
                return ticket
        print('该罚单编号不存在!')
        return

    def show_unpaid_ticket(self):
        print('--------未缴纳罚单--------')
        for ticket in self.ticket_list:
            if ticket.statu == '0':
                print(ticket)
        print('------------------------')
        return

    def show_all_ticket(self):
        print('--------所有罚单信息--------')
        print('编号\t姓名\t\t\t身份证号\t\t驾照等级\t\t手机号\t\t车辆牌号\t车辆类型\t违法行为\t缴纳情况')
        for ticket in self.ticket_list:
            print(ticket)
        print('-------------------------')
        return

    def run(self):
        while True:
            a = input('请输入要执行的操作(序号): ')
            if a == '1':
                self.create_ticket()
            elif a == '2':
                self.delete_ticket()
            elif a == '3':
                self.update_ticket()
            elif a == '4':
                self.select_ticket()
            elif a == '5':
                self.show_unpaid_ticket()
            elif a == '6':
                self.show_all_ticket()
            elif a == '0':
                print('Good Bye!')
                exit()
            else:
                print('输入错误!请重新输入要执行的操作(序号): ')

if __name__ == '__main__':
    Te = Ticket_exec()
    Te.run()
