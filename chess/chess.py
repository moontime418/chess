from itertools import count

line0=[' ','a','b','c','d','e','f','g','h']
line1=['1','♜','♞','♝','♚','♛','♝','♞','♜']
line2=['2','♟','♟','♟','♟','♟','♟','♟','♟']
line3=['3','□','■','□','■','□','■','□','■']
line4=['4','■','□','■','□','■','□','■','□']
line5=['5','□','■','□','■','□','■','□','■']
line6=['6','■','□','■','□','■','□','■','□']
line7=['7','♙','♙','♙','♙','♙','♙','♙','♙']
line8=['8','♖','♘','♗','♕','♔','♗','♘','♖']

change_white=['♙','♖','♘','♗','♔']
change_black=['♟','♜','♞','♝','♛']

def print_board():
    for i in range(9):
        print('\t'.join(globals()[f'line{i}']))

def change():
    if choice_height % 2 == 0:
        if choice_width % 2 == 0:
            globals()[f'line{choice_height}'][choice_width] = '□'
        else:
            globals()[f'line{choice_height}'][choice_width] = '■'
    else:
        if choice_width % 2 == 0:
            globals()[f'line{choice_height}'][choice_width] = '■'
        else:
            globals()[f'line{choice_height}'][choice_width] = '□'

turn=0
answer=0    #기본세팅

while True:

    print()
    print_board()
    answer=0

    if turn%2==0:    #백 차례

        while answer==0:    #백 이동 말 입력
            print("백 차례입니다")
            choice = input('이동할 말을 입력하세요 (예: a2) : ')
            choice_width = ord(choice[0])-96
            choice_height = int(choice[1])

            if globals()[f'line{choice_height}'][choice_width] in ['♙','♖','♘','♗','♕','♔']:    #백 이동 말 검토
                answer=1
            else:
                print('옳지 않은 입력입니다')

        while answer==1:    #백 이동 장소 입력
            error=0
            go = input('이동할 곳을 입력하세요 (예: a2) : ')
            if go==('back'):
                answer=0
                break
            go_width = ord(go[0]) - 96
            go_height =int(go[1])

            if globals()[f'line{go_height}'][go_width] in ['♙','♖','♘','♗','♕','♔']:
                print('옳지 않은 입력입니다')

            if globals()[f'line{choice_height}'][choice_width] == '♙':    #폰 이동

                if choice_height == 7 and choice_width == go_width:    #폰 첫 직선 이동

                    if 0<choice_height-go_height<3:
                        for i in range(1,choice_height-go_height):
                            if globals()[f'line{choice_height-i}'][choice_width] in ['■','□']:
                                continue
                            else:
                                print('옳지 않은 입력입니다')
                                break

                        globals()[f'line{go_height}'][go_width]='♙'
                        change()
                        answer=3
                        turn+=1

                    else:
                        print('옳지 않은 입력입니다')
                        break

                elif choice_height !=7 and choice_width == go_width:    #폰 이후 직선 이동
                    if choice_height-go_height == 1:
                        if globals()[f'line{go_height}'][go_width] in ['■', '□']:
                            if go_height==1:
                                change=int(input("원하는 기물 번호를 선택하세요 (♙,♖,♘,♗,♔) : "))
                                globals()[f'line{go_height}'][go_width] = change_white[change-1]
                                change()
                                answer = 3
                                turn+= 1
                            else:
                                globals()[f'line{go_height}'][go_width] = '♙'
                                change()
                                answer = 3
                                turn+= 1
                        else:
                            print('옳지 않은 입력입니다')
                            break
                    else:
                        print('옳지 않은 입력입니다')
                        break

                elif choice_height-go_height == 1 and abs(choice_width-go_width) == 1:
                    if globals()[f'line{go_height}'][go_width] in ['♟','♜','♞','♝','♚','♛']:
                        if globals()[f'line{go_height-1}'][go_width] in ['■','□']:
                            globals()[f'line{go_height}'][go_width] = '♙'
                            change()
                            answer = 3
                            turn+= 1
                        else:
                            print('옳지 않은 입력입니다')
                            break
                    else:
                        print('옳지 않은 입력입니다')
                        break
                else:
                    print('옳지 않은 입력입니다')
                    break

    elif turn%2==1:    #흑 차례

        while answer==0:    #흑 이동 말 입력
            print("흑 차례입니다")
            choice = input('이동할 말을 입력하세요 (예: a2) : ')
            choice_width = ord(choice[0])-96
            choice_height = int(choice[1])

            if globals()[f'line{choice_height}'][choice_width] in ['♟','♜','♞','♝','♚','♛']:    #흑 이동 말 검토
                answer=1
            else:
                print('옳지 않은 입력입니다')


