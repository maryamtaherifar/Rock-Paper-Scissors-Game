import streamlit as st
import random

st.title('🎮 Rock Paper Scissors')
# Initialization
limit_score = int(st.number_input("Please enter the score's limit of the game: ", min_value=1, value=3, step=1))
if 'limit' not in st.session_state:
    st.session_state.limit = limit_score
else:
    if st.session_state.limit != int(limit_score):
        st.session_state.limit = int(limit_score)

if 'scores' not in st.session_state:
    st.session_state.scores = {'You': 0, 'Computer': 0}

if 'game_over' not in st.session_state:
    st.session_state.game_over = False

if 'last_round' not in st.session_state:
    st.session_state.last_round = {'You': None, 'Computer': None}


def play_round(user_choice):

    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice, computer_choice) in [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]:
        st.session_state.scores['You'] += 1
    else:
        st.session_state.scores['Computer'] += 1

    st.session_state.last_round['You'] = user_choice
    st.session_state.last_round['Computer'] = computer_choice


def reset_game():
    st.session_state.scores = {'You': 0, 'Computer': 0}
    st.session_state.game_over = False
    st.session_state.last_round = {"You": None, "Computer": None}


def run():
    if not st.session_state.game_over:
        st.write('Choose your move:')

        _, col1, col2, col3, _ = st.columns([2, 1, 1, 1, 2])
        if col1.button('Rock'):
            play_round('Rock')
        if col2.button('Paper'):
            play_round('Paper')
        if col3.button('Scissors'):
            play_round('Scissors')

        if st.session_state.limit in st.session_state.scores.values():
            st.session_state.game_over = True
            st.rerun()
        lr = st.session_state.last_round
        if lr['You']:
            st.write(f"""Your choice: {lr['You']}
                    \nThe computer choice: {lr['Computer']}
                    \nScores:
                    \nYou: {st.session_state.scores['You']}
                    \nComputer: {st.session_state.scores['Computer']}""")
    else:
        st.subheader("🎉Game Over!🎉")
        st.write(f"""Scores:
                    \nYou: {st.session_state.scores['You']}
                    \nComputer: {st.session_state.scores['Computer']}
                """)
        if st.session_state.scores['You'] == st.session_state.limit:
            st.write('🥇 You win!')
        else:
            st.write('🥇 Computer wins!')
        if st.button('Play again'):
            reset_game()


if __name__ == '__main__':
    run()