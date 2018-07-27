import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 順運動学の計算

def fk(L, th):
    # 各リンクの長さと関節角度の取得
    l1, l2, l3 = L
    th1, th2, th3 = th

    # リンク1の手先
    x1 = l1 * np.cos(th1)
    y1 = l1 * np.sin(th1)

    # リンク2の手先
    x2 = x1 + l2 * np.cos(th1 + th2)
    y2 = y1 + l2 * np.sin(th1 + th2)

    # リンク3の手先
    x3 = x2 + l3 * np.cos(th1 + th2 + th3)
    y3 = y2 + l3 * np.sin(th1 + th2 + th3)

    # 手先位置をNumPy配列に格納して返す
    return np.array([[0, 0], [x1, y1], [x2, y2], [x3, y3]])

def calculate_arms():
    p = fk(L, th)

    # 手先位置を更新
    graph.set_data(p.T[0], p.T[1])
    graph.set_linestyle('-')
    graph.set_linewidth(5)
    graph.set_marker('o')
    graph.set_markerfacecolor('g')
    graph.set_markeredgecolor('g')
    graph.set_markersize(15)

    # グラフの再描画


def update_th1(slider_val):
    # 関節1の角度を更新
    th[0] = np.radians([slider_val])
    calculate_arms()
    fig.canvas.draw_idle()

def update_th2(slider_val):
    # 関節1の角度を更新
    th[1] = np.radians([slider_val])
    calculate_arms()
    fig.canvas.draw_idle()

def update_th3(slider_val):
    # 関節1の角度を更新
    th[2] = np.radians([slider_val])
    calculate_arms()
    fig.canvas.draw_idle()




def main():
    # スライダーの表示位置
    slider1_pos = plt.axes([0.1, 0.09, 0.8, 0.03])
    slider2_pos = plt.axes([0.1, 0.05, 0.8, 0.03])
    slider3_pos = plt.axes([0.1, 0.01, 0.8, 0.03])

    # Sliderオブジェクトのインスタンス作成
    threshold_slider1 = Slider(slider1_pos, 'th1', 0, 180)
    threshold_slider2 = Slider(slider2_pos, 'th2', 0, 180)
    threshold_slider3 = Slider(slider3_pos, 'th3', 0, 180)

    # スライダーの値が変更された場合の処理を呼び出し
    threshold_slider1.on_changed(update_th1)
    threshold_slider2.on_changed(update_th2)
    threshold_slider3.on_changed(update_th3)
    calculate_arms()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # リンク1, 2の長さ
    L = [0.5, 0.5, 0.5]

    # 第1, 2の関節角度
    th = np.radians([90, 0, 0])

    # 順運動学の計算
    p = fk(L, th)

    # グラフ描画位置の設定
    fig, ax = plt.subplots()
    plt.axes().set_aspect('equal', 'datalim')
    plt.subplots_adjust(left=0.1, bottom=0.20)
    plt.xlim([-1.5, 1.5])
    plt.ylim([-0.8, 1.8])
    # グラフ描画
    plt.grid()
    graph, = plt.plot(p.T[0], p.T[1])
    main()