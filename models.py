# coding: UTF-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

class Model_takami():

    @classmethod

    def __init__(self):

        # モデルの中の訓練されたクラス
        self.classNames = {1: 'black_uron', 2: 'tyouseimeitai', 3: 'match',
                  4: 'orangina100', 5: 'etc', 6: 'etc', 7: 'etc',
                  8: 'cola', 9: 'etc', 10: 'etc', 11: 'etc', 12: 'etc', 13: 'etc', 14: 'etc', 15: 'etc', 16: 'etc'}

        # モデルの読み込み
        self.model = cv2.dnn.readNetFromTensorflow('model_takami/frozen_inference_graph.pb',
                                          'model_takami/v1_graph_aws4.pbtxt')

    def predict(self,img='img/image.jpg'):

        lst_item=[]

        # テスト画像の読み込み
        image = cv2.imread(img)

        # 画像の縦と横サイズを取得
        image_height, image_width = image.shape[:2]

        # Imageからblobに変換する
        self.model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))

        # 画像から物体検出を行う
        output = self.model.forward()

        # outputは[1:1:100:7]のリストになっているため、後半の2つを取り出す
        detections = output[0, 0, :, :]

        # detectionには[?,id番号、予測確率、Xの開始点、Yの開始点、Xの終了点、Yの終了点]が入っている。
        for detection in detections:
        # 予測確率を取り出し0.5以上か判定する。0.5以上であれば物体が正しく検出されたと判定する。
            confidence = detection[2]
            if confidence > .9:
                # id番号を取り出し、辞書からクラス名を取り出す。
                idx = detection[1]
                class_name = self.classNames[idx]

                # 検出された物体の名前を表示
                print('id:{} | {:.1f}% | {}'.format(int(idx), confidence*100, class_name))

                # 予測値に元の画像サイズを掛けて、四角で囲むための4点の座標情報を得る
                axis = detection[3:7] * (image_width, image_height, image_width, image_height)

                # floatからintに変換して、変数に取り出す。画像に四角や文字列を書き込むには、座標情報はintで渡す必要がある。
                (start_X, start_Y, end_X, end_Y) = axis.astype(np.int)[:4]

                # (画像、開始座標、終了座標、色、線の太さ)を指定
                #cv2.rectangle(image, (start_X, start_Y), (end_X, end_Y), (23, 230, 210), thickness=2)
                cv2.rectangle(image, (start_X, start_Y), (end_X, end_Y), (0, 0, 255), thickness=2)

                # (画像、文字列、開始座標、フォント、文字サイズ、色)を指定
                cv2.putText(image, class_name, (start_X, start_Y + int((end_Y - start_Y)/2)), cv2.FONT_HERSHEY_COMPLEX, (.001 * image_width),
                            (23, 230, 210), 2)

                lst_item.append(class_name)

        #cv2.imshow('image', image)
        cv2.imwrite("img/result.jpg", image)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        # 描画
        #img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #plt.figure(figsize=(7, 7))
        #plt.imshow(img_rgb);

        return lst_item

class Model_16_half():

    @classmethod

    def __init__(self):

        # モデルの中の訓練されたクラス
        self.classNames = {1: 'black_uron', 2: 'tyouseimeitai', 3: 'match',
                  4: 'orangina100', 5: 'etc', 6: 'etc', 7: 'etc',
                  8: 'cola', 9: 'etc', 10: 'etc', 11: 'etc', 12: 'etc', 13: 'etc', 14: 'etc', 15: 'etc', 16: 'etc'}

        # モデルの読み込み
        self.model = cv2.dnn.readNetFromTensorflow('model_16_3500/frozen_inference_graph.pb',
                                          'model_16_3500/v1_graph_aws3.pbtxt')

    def predict(self,img='img/image.jpg'):

        lst_item=[]

        # テスト画像の読み込み
        image = cv2.imread(img)

        # 画像の縦と横サイズを取得
        image_height, image_width = image.shape[:2]

        # Imageからblobに変換する
        self.model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))

        # 画像から物体検出を行う
        output = self.model.forward()

        # outputは[1:1:100:7]のリストになっているため、後半の2つを取り出す
        detections = output[0, 0, :, :]

        # detectionには[?,id番号、予測確率、Xの開始点、Yの開始点、Xの終了点、Yの終了点]が入っている。
        for detection in detections:
        # 予測確率を取り出し0.5以上か判定する。0.5以上であれば物体が正しく検出されたと判定する。
            confidence = detection[2]
            if confidence > .5:
                # id番号を取り出し、辞書からクラス名を取り出す。
                idx = detection[1]
                class_name = self.classNames[idx]

                # 検出された物体の名前を表示
                print('id:{} | {:.1f}% | {}'.format(int(idx), confidence*100, class_name))

                # 予測値に元の画像サイズを掛けて、四角で囲むための4点の座標情報を得る
                axis = detection[3:7] * (image_width, image_height, image_width, image_height)

                # floatからintに変換して、変数に取り出す。画像に四角や文字列を書き込むには、座標情報はintで渡す必要がある。
                (start_X, start_Y, end_X, end_Y) = axis.astype(np.int)[:4]

                # (画像、開始座標、終了座標、色、線の太さ)を指定
                #cv2.rectangle(image, (start_X, start_Y), (end_X, end_Y), (23, 230, 210), thickness=2)
                cv2.rectangle(image, (start_X, start_Y), (end_X, end_Y), (0, 0, 255), thickness=2)

                # (画像、文字列、開始座標、フォント、文字サイズ、色)を指定
                cv2.putText(image, class_name, (start_X, start_Y + int((end_Y - start_Y)/2)), cv2.FONT_HERSHEY_COMPLEX, (.001 * image_width),
                            (23, 230, 210), 2)

                lst_item.append(class_name)

        #cv2.imshow('image', image)
        cv2.imwrite("img/result.jpg", image)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        # 描画
        #img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #plt.figure(figsize=(7, 7))
        #plt.imshow(img_rgb);

        return lst_item

class Model_B():

    @classmethod

    def __init__(self):

        # モデルの中の訓練されたクラス
        self.classNames = {1: 'black_uron', 2: 'tyouseimeitai', 3: 'match',
                  4: 'orangina100', 5: 'etc', 6: 'etc', 7: 'etc',
                  8: 'cola', 9: 'etc'}

        # モデルの読み込み
        self.model = cv2.dnn.readNetFromTensorflow('model_B/frozen_inference_graph.pb',
                                          'model_B/v1_graph_aws.pbtxt')

    def predict(self,img='img/image.jpg'):

        lst_item=[]

        # テスト画像の読み込み
        image = cv2.imread(img)

        # 画像の縦と横サイズを取得
        image_height, image_width = image.shape[:2]

        # Imageからblobに変換する
        self.model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))

        # 画像から物体検出を行う
        output = self.model.forward()

        # outputは[1:1:100:7]のリストになっているため、後半の2つを取り出す
        detections = output[0, 0, :, :]

        # detectionには[?,id番号、予測確率、Xの開始点、Yの開始点、Xの終了点、Yの終了点]が入っている。
        for detection in detections:
        # 予測確率を取り出し0.5以上か判定する。0.5以上であれば物体が正しく検出されたと判定する。
            confidence = detection[2]
            if confidence > .5:
                # id番号を取り出し、辞書からクラス名を取り出す。
                idx = detection[1]
                class_name = self.classNames[idx]

                # 検出された物体の名前を表示
                print('id:{} | {:.1f}% | {}'.format(int(idx), confidence*100, class_name))

                # 予測値に元の画像サイズを掛けて、四角で囲むための4点の座標情報を得る
                axis = detection[3:7] * (image_width, image_height, image_width, image_height)

                # floatからintに変換して、変数に取り出す。画像に四角や文字列を書き込むには、座標情報はintで渡す必要がある。
                (start_X, start_Y, end_X, end_Y) = axis.astype(np.int)[:4]

                # (画像、開始座標、終了座標、色、線の太さ)を指定
                #cv2.rectangle(image, (start_X, start_Y), (end_X, end_Y), (23, 230, 210), thickness=2)
                cv2.rectangle(image, (start_X, start_Y), (end_X, end_Y), (0, 0, 255), thickness=2)

                # (画像、文字列、開始座標、フォント、文字サイズ、色)を指定
                cv2.putText(image, class_name, (start_X, start_Y + int((end_Y - start_Y)/2)), cv2.FONT_HERSHEY_COMPLEX, (.001 * image_width),
                            (23, 230, 210), 2)

                lst_item.append(class_name)

        #cv2.imshow('image', image)
        cv2.imwrite("img/result.jpg", image)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        # 描画
        #img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #plt.figure(figsize=(7, 7))
        #plt.imshow(img_rgb);

        return lst_item
