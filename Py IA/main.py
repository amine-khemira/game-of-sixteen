from pynput import keyboard
from board import board
b = board()
b.shuffle()
def main():
    
    b.refresh()
    print(b)
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def on_press(key):
    b.refresh()


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key ==keyboard.Key.up:
        b.board, b.empty_loc = b.move_up(b.board,b.empty_loc)
    elif key ==keyboard.Key.right:
        b.board, b.empty_loc = b.move_right(b.board,b.empty_loc)
    elif key ==keyboard.Key.down:
        b.board, b.empty_loc = b.move_down(b.board,b.empty_loc)
    elif key ==keyboard.Key.left:
        b.board, b.empty_loc = b.move_left(b.board,b.empty_loc)
    elif key ==keyboard.Key.shift:
        b.solve()

    return b.refresh()   
        
        





def main():

    import tkinter as tk

    window = tk.Tk()

    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.FLAT,
                borderwidth=25
                
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=b.board[i][j])
            label.pack()

    window.mainloop()  
    print(b)
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()



if __name__ == "__main__":
    main()
