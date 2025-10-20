from termcolor import cprint

def end_of_game(scores, limit):
    if limit in scores.values():
        reversed_scores = {score: player for player, score in scores.items()}
        cprint(f"\n🎉Game over!🎉\nThe winner: {reversed_scores[limit]} 🥇", color='white', on_color='on_light_magenta')
        cprint('\nScores:', color='white', on_color='on_green')
        for p, s in scores.items():
            cprint(f"{p}: {s}", color='white', on_color='on_green')
        return True
    return False