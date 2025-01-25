import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Healthy Test']
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Home':
        st.markdown(
            """
            <h1 style='text-align: center;'>Empower Your Health – Start Today!</h1>

            <br>

            <h4 style='text-align: justify;'>Do You Know How Healthy You Are?</h4>
            <p style='text-align: justify;'>Your <strong>health</strong> is the foundation of everything, such as energy, happiness, and success. However, in the rush of life, it's easy to forget what your body really needs. That's why we're here to help you take control.</p>
            
            <br>

            <h4 style='text-align: justify;'>Understand Your Health with One Simple Step</h4>
            <p style='text-align: justify;'>With our health score tool, you’ll get a clear picture of your well-being. Are you getting enough exercise? Is your diet supporting your goals? This is your chance to uncover what’s working and what’s not.</p>
            
            <br>

            <h4 style='text-align: justify;'>Why Knowing Your Health Score Matters</h4>
            <ul>
                <li>Prevent potential health risks before they become serious.</li>
                <li>Stay energized and productive in your daily life.</li>
                <li>Build a lifestyle that promotes long-term happiness and vitality.</li>
            </ul>

            <br>

            <p style='text-align: center;'><strong>Take the First Step Today Because You Deserve to Feel Your Best</strong></p>
            """, 
            unsafe_allow_html=True
        )

    elif choice == "Healthy Test":
        run_ml_app()

if __name__ == '__main__':
    main()
