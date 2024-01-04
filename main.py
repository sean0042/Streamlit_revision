import streamlit as st

def intro():

    import streamlit as st

    st.write("# 수정 (Revision)")
    st.sidebar.success("선생님 성함을 골라주세요.")

    st.markdown(
        """

        해당 데이터셋은 

        1. 수정 (Revision)   👈
        2. 검토 (Examination)

        두 단계로 진행됩니다.

        ---

        - 해당 페이지는, :blue[첫 번째] 평가에 대한 :blue[수정] 단계 입니다.

        - 먼저, 해당 링크의 구글 스프레드 시트를 켜주세요. 

        - 다음, 왼쪽 사이드바에서 선생님의 성함을 골라주세요. 한 분 당 50개의 데이터를 보게 됩니다.

        - 오른쪽 위에 메뉴 (...) 의 setting에서 wide screen을 선택하시면 해당 링크의 width가 넓어집니다. 편하신 방법으로 사용하시면 됩니다.
    """
    )

def cha():
    import streamlit as st
    import pandas as pd


    st.markdown(f"# {list(page_names_to_funcs.keys())[2]} 선생님")


    @st.cache_data
    def from_data_file(filename):
        return pd.read_csv(filename)
    
    filtered_df = from_data_file("stage7_filtered_df.csv")
    step3 = from_data_file("stage7_step3.csv")
    patient_id = list(step3["Patient_ID"].values)
    patient_id_1 = patient_id[::3]


    index = st.number_input(
    "**총 1부터 :red[50] 까지 있습니다. (오른쪽 + - 버튼으로 조절하거나 숫자를 입력한 후 Enter)**", 1, 50)
    index = index-1
    st.markdown("---")
    st.markdown(f"Index : :blue[{index+1}]")
    st.markdown(f"Patient ID : :blue[{patient_id_1[index]}]")
    


    tmp_df = filtered_df[filtered_df["subject_id"]==patient_id_1[index]]
    st.markdown(f"환자 노트 총 :blue[{len(tmp_df)}]개")

    st.markdown("---")

    note_len = len(tmp_df)
    note_choice = [f"Note {i+1} out of {note_len}" for i in range(note_len)]
    option = st.selectbox(
        '몇 번째 노트를 보실 지 선택해주세요',
        note_choice)
    st.write("Note가 두 개 이상인 경우 앞에 있는 노트는 chartdate 기준으로 먼저 발생한 노트입니다.")
    st.markdown(f":red[{option}]")
    
    text = tmp_df["new_text"].values[note_choice.index(option)].replace("\n","  \n  ").replace("# ","#")
    st.info(text)

    question = step3[step3["Patient_ID"]==patient_id_1[index]]["Question"].values[0]
    choice_A = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_A"].values[0]
    choice_B = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_B"].values[0]
    choice_C = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_C"].values[0]
    choice_D = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_D"].values[0]
    choice_E = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_E"].values[0]
    answer = step3[step3["Patient_ID"]==patient_id_1[index]]["Answer"].values[0]
    reason = step3[step3["Patient_ID"]==patient_id_1[index]]["Reason"].values[0]

    with st.sidebar:
        st.write("---")
        st.warning(f"**Question** : {question}")
        st.success(f"**Choice A** : {choice_A}")
        st.success(f"**Choice B** : {choice_B}")
        st.success(f"**Choice C** : {choice_C}")
        st.success(f"**Choice D** : {choice_D}")
        st.success(f"**Choice E** : {choice_E}")
        st.error(f"**Answer** : {answer}")
        st.error(f"**Reason** : {reason}")


def kim():
    import streamlit as st
    import pandas as pd


    st.markdown(f"# {list(page_names_to_funcs.keys())[1]} 선생님")


    @st.cache_data
    def from_data_file(filename):
        return pd.read_csv(filename)
    
    filtered_df = from_data_file("stage7_filtered_df.csv")
    step3 = from_data_file("stage7_step3.csv")
    patient_id = list(step3["Patient_ID"].values)
    patient_id_1 = patient_id[1::3]


    index = st.number_input(
    "**총 1부터 :red[50] 까지 있습니다. (오른쪽 + - 버튼으로 조절하거나 숫자를 입력한 후 Enter)**", 1, 50)
    index = index-1
    st.markdown("---")
    st.markdown(f"Index : :blue[{index+1}]")
    st.markdown(f"Patient ID : :blue[{patient_id_1[index]}]")
    


    tmp_df = filtered_df[filtered_df["subject_id"]==patient_id_1[index]]
    st.markdown(f"환자 노트 총 :blue[{len(tmp_df)}]개")

    st.markdown("---")

    note_len = len(tmp_df)
    note_choice = [f"Note {i+1} out of {note_len}" for i in range(note_len)]
    option = st.selectbox(
        '몇 번째 노트를 보실 지 선택해주세요',
        note_choice)
    st.write("Note가 두 개 이상인 경우 앞에 있는 노트는 chartdate 기준으로 먼저 발생한 노트입니다.")
    st.markdown(f":red[{option}]")
    
    text = tmp_df["new_text"].values[note_choice.index(option)].replace("\n","  \n  ").replace("# ","#")
    st.info(text)

    question = step3[step3["Patient_ID"]==patient_id_1[index]]["Question"].values[0]
    choice_A = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_A"].values[0]
    choice_B = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_B"].values[0]
    choice_C = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_C"].values[0]
    choice_D = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_D"].values[0]
    choice_E = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_E"].values[0]
    answer = step3[step3["Patient_ID"]==patient_id_1[index]]["Answer"].values[0]
    reason = step3[step3["Patient_ID"]==patient_id_1[index]]["Reason"].values[0]

    with st.sidebar:
        st.write("---")
        st.warning(f"**Question** : {question}")
        st.success(f"**Choice A** : {choice_A}")
        st.success(f"**Choice B** : {choice_B}")
        st.success(f"**Choice C** : {choice_C}")
        st.success(f"**Choice D** : {choice_D}")
        st.success(f"**Choice E** : {choice_E}")
        st.error(f"**Answer** : {answer}")
        st.error(f"**Reason** : {reason}")


def yun():
    import streamlit as st
    import pandas as pd


    st.markdown(f"# {list(page_names_to_funcs.keys())[3]} 선생님")


    @st.cache_data
    def from_data_file(filename):
        return pd.read_csv(filename)
    
    filtered_df = from_data_file("stage7_filtered_df.csv")
    step3 = from_data_file("stage7_step3.csv")
    patient_id = list(step3["Patient_ID"].values)
    patient_id_1 = patient_id[2::3]


    index = st.number_input(
    "**총 1부터 :red[50] 까지 있습니다. (오른쪽 + - 버튼으로 조절하거나 숫자를 입력한 후 Enter)**", 1, 50)
    index = index-1
    st.markdown("---")
    st.markdown(f"Index : :blue[{index+1}]")
    st.markdown(f"Patient ID : :blue[{patient_id_1[index]}]")
    


    tmp_df = filtered_df[filtered_df["subject_id"]==patient_id_1[index]]
    st.markdown(f"환자 노트 총 :blue[{len(tmp_df)}]개")

    st.markdown("---")

    note_len = len(tmp_df)
    note_choice = [f"Note {i+1} out of {note_len}" for i in range(note_len)]
    option = st.selectbox(
        '몇 번째 노트를 보실 지 선택해주세요',
        note_choice)
    st.write("Note가 두 개 이상인 경우 앞에 있는 노트는 chartdate 기준으로 먼저 발생한 노트입니다.")
    st.markdown(f":red[{option}]")
    
    text = tmp_df["new_text"].values[note_choice.index(option)].replace("\n","  \n  ").replace("# ","#")
    st.info(text)

    question = step3[step3["Patient_ID"]==patient_id_1[index]]["Question"].values[0]
    choice_A = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_A"].values[0]
    choice_B = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_B"].values[0]
    choice_C = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_C"].values[0]
    choice_D = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_D"].values[0]
    choice_E = step3[step3["Patient_ID"]==patient_id_1[index]]["Choice_E"].values[0]
    answer = step3[step3["Patient_ID"]==patient_id_1[index]]["Answer"].values[0]
    reason = step3[step3["Patient_ID"]==patient_id_1[index]]["Reason"].values[0]

    with st.sidebar:
        st.write("---")
        st.warning(f"**Question** : {question}")
        st.success(f"**Choice A** : {choice_A}")
        st.success(f"**Choice B** : {choice_B}")
        st.success(f"**Choice C** : {choice_C}")
        st.success(f"**Choice D** : {choice_D}")
        st.success(f"**Choice E** : {choice_E}")
        st.error(f"**Answer** : {answer}")
        st.error(f"**Reason** : {reason}")


page_names_to_funcs = {
    "홈": intro,
    "김광현": kim,
    "차동철": cha,
    "윤한결": yun
}

demo_name = st.sidebar.selectbox("선생님 성함을 골라주세요", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()