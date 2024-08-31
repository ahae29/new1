{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnqK+8enJY7gGjD2+K+8sS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ahae29/new1/blob/main/s5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SosskziZAZ20"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from sklearn.linear_model import LinearRegression\n",
        "import numpy as np\n",
        "\n",
        "# 데이터 준비 (공부 시간과 점수)\n",
        "data = {\n",
        "    'study_hours': [1, 2, 3, 4, 5, 6],\n",
        "    'scores': [50, 60, 70, 80, 90, 100]\n",
        "}\n",
        "\n",
        "# 데이터프레임 생성\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# 선형 회귀 모델 훈련\n",
        "X = df[['study_hours']]\n",
        "y = df['scores']\n",
        "model = LinearRegression()\n",
        "model.fit(X, y)\n",
        "\n",
        "# Streamlit 앱 설정\n",
        "st.title(\"공부 시간에 따른 점수 예측기\")\n",
        "\n",
        "# 사용자 입력\n",
        "study_hours = st.number_input(\"공부 시간을 입력하세요 (시간):\", min_value=0.0, max_value=10.0, step=0.1)\n",
        "\n",
        "# 점수 예측\n",
        "predicted_score = model.predict(np.array([[study_hours]]))[0]\n",
        "\n",
        "# 결과 출력\n",
        "st.write(f\"예상 점수: {predicted_score:.2f}\")\n"
      ]
    }
  ]
}