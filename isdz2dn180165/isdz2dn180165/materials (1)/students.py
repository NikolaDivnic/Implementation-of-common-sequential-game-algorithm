import math
import random

from agents import Agent


# Example agent, behaves randomly.
# ONLY StudentAgent and his descendants have a 0 id. ONLY one agent of this type must be present in a game.
# Agents from bots.py have successive ids in a range from 1 to number_of_bots.


class StudentAgent(Agent):
    def __init__(self, position, file_name):
        super().__init__(position, file_name)
        self.id = 0

    @staticmethod
    def kind():
        return '0'

    # Student shall override this method in derived classes.
    # This method should return one of the legal actions (from the Actions class) for the current state.
    # state - represents a state object.
    # max_levels - maximum depth in a tree search. If max_levels eq -1 than the tree search depth is unlimited.
    def get_next_action(self, state, max_levels):
        actions = self.get_legal_actions(state)  # equivalent of state.get_legal_actions(self.id)
        chosen_action = actions[random.randint(0, len(actions) - 1)]
        # Example of a new_state creation (for a chosen_action of a self.id agent):
        # new_state = state.apply_action(self.id, chosen_action)
        return chosen_action


class MinimaxAgent(StudentAgent):
    def get_next_action(self, state, max_levels):

        actions = self.get_legal_actions(state)
        states_list = [state.apply_action(self.id, act) for act in actions]
        coll = list(zip(actions, states_list))
        akcija = None
        vrednost = -math.inf
        listaPoraza = []
        for c in coll:
            c[1].adjust_win_loss()
            if c[1].is_win():
                akcija = c[0]
                return akcija
            if c[1].is_loss():
                listaPoraza.append(c[0])
            else:
                r = self.rekurzivna(c[1], 0, max_levels)
                if r == 1:
                    akcija = c[0]
                    return akcija
                if r > vrednost:
                    vrednost = r
                    akcija = c[0]
                if r == -1:
                    listaPoraza.append(c[0])
        if vrednost > -1:
            return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NORTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NE':
                akcija = listaPoraza[i]
                return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'EAST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SE':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SOUTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SW':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'WEST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NW':
                akcija = listaPoraza[i]
                return akcija

        return listaPoraza[0]

    def rekurzivna(self, state, playerMax, max_levels):

        if playerMax == 1:
            if state.is_win():
                return 1
            if state.is_loss():
                return -1
            actions = self.get_legal_actions(state)
            states_list = [state.apply_action(self.id, act) for act in actions]
            coll = list(zip(actions, states_list))
            if max_levels == 0:
                return len(coll) / 10
            vrednost = -1
            for c in coll:
                c[1].adjust_win_loss()
                if c[1].is_win():
                    return 1
                if not c[1].is_loss():
                    r = self.rekurzivna(c[1], 0, max_levels - 1)
                    if r == 1:
                        return 1
                    if r > vrednost:
                        vrednost = r

            return vrednost
        else:
            if state.is_win():
                return -1
            if state.is_loss():
                return 1
            actions = state.agents[1].get_legal_actions(state)
            states_list = [state.apply_action(state.agents[1].id, act) for act in actions]
            coll = list(zip(actions, states_list))
            vrednost = 1
            if max_levels == 0:
                return -len(coll) / 10
            for c in coll:
                c[1].adjust_win_loss()
                if c[1].is_win():
                    return -1
                if not c[1].is_loss():
                    r = self.rekurzivna(c[1], 1, max_levels - 1)
                    if r == -1:
                        return -1
                    if vrednost > r:
                        vrednost = r

            return vrednost


class MinimaxABAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        actions = self.get_legal_actions(state)
        states_list = [state.apply_action(self.id, act) for act in actions]
        coll = list(zip(actions, states_list))
        score = -1
        akcija = None
        listaPoraza = []
        alpha = -math.inf
        beta = +math.inf
        for c in coll:
            c[1].adjust_win_loss()
            if c[1].is_win():
                akcija = c[0]
                return akcija
            if c[1].is_loss() and score == -1:
                listaPoraza.append(c[0])
            else:
                r = self.rekurzivna(c[1], 0, alpha, beta, max_levels)
                if r == 1:
                    akcija = c[0]
                    return akcija

                if r == -1:
                    listaPoraza.append(c[0])
                else:
                    if r > score:
                        score = r
                        akcija = c[0]

        if score > -1:
            return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NORTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NE':
                akcija = listaPoraza[i]
                return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'EAST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SE':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SOUTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SW':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'WEST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NW':
                akcija = listaPoraza[i]
                return akcija

        return akcija

    def rekurzivna(self, state, playerMax, alpha, beta, max_levels):

        if playerMax == 1:
            if state.is_win():
                return 1
            if state.is_loss():
                return -1
            actions = self.get_legal_actions(state)
            states_list = [state.apply_action(self.id, act) for act in actions]
            coll = list(zip(actions, states_list))
            score = -1
            if max_levels == 0:
                return len(coll) / 10
            for c in coll:
                c[1].adjust_win_loss()
                if c[1].is_win():
                    return 1
                if not c[1].is_loss():
                    r = self.rekurzivna(c[1], 0, alpha, beta, max_levels-1)
                    alpha = max(alpha, r)
                    score = max(score, r)
                    if r == 1:
                        return 1
                    if alpha >= beta:
                        break

            return score
        else:
            if state.is_win():
                return -1
            if state.is_loss():
                return 1
            actions = state.agents[1].get_legal_actions(state)
            states_list = [state.apply_action(state.agents[1].id, act) for act in actions]
            coll = list(zip(actions, states_list))
            score = 1
            if max_levels == 0:
                return -len(coll) / 10
            for c in coll:
                c[1].adjust_win_loss()
                if c[1].is_win():
                    return -1
                if not c[1].is_loss():
                    r = self.rekurzivna(c[1], 1, alpha, beta, max_levels-1)
                    beta = min(beta, r)
                    score = min(score, r)
                    if r == -1:
                        return -1
                    if alpha >= beta:
                        break

            return score


class ExpectAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        actions = self.get_legal_actions(state)
        states_list = [state.apply_action(self.id, act) for act in actions]
        coll = list(zip(actions, states_list))
        akcija = None
        vrednost = -math.inf
        listaPoraza = []
        for c in coll:
            c[1].adjust_win_loss()
            if c[1].is_win():
                akcija = c[0]
                return akcija
            if c[1].is_loss():
                listaPoraza.append(c[0])
            else:
                r = self.rekurzivna(c[1], 0, max_levels)
                if r == 1:
                    akcija = c[0]
                    return akcija
                if r == -1:
                    listaPoraza.append(c[0])
                else:
                    if vrednost < r:
                        vrednost = r
                        akcija = c[0]

        if vrednost > -1:
            return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NORTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NE':
                akcija = listaPoraza[i]
                return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'EAST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SE':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SOUTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SW':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'WEST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NW':
                akcija = listaPoraza[i]
                return akcija

        return listaPoraza[0]

    def rekurzivna(self, state, playerMax, max_levels):

        if playerMax == 1:
            if state.is_win():
                return 1
            if state.is_loss():
                return -1
            actions = self.get_legal_actions(state)
            states_list = [state.apply_action(self.id, act) for act in actions]
            coll = list(zip(actions, states_list))
            vrednost = -1
            if max_levels == 0:
                return len(coll) / 10
            for c in coll:
                c[1].adjust_win_loss()
                if c[1].is_win():
                    return 1

                r = self.rekurzivna(c[1], 0,max_levels-1)
                if r == 1:
                    return 1
                vrednost = max(vrednost, r)
            return vrednost
        else:
            if state.is_win():
                return -1
            if state.is_loss():
                return 1
            actions = state.agents[1].get_legal_actions(state)
            states_list = [state.apply_action(state.agents[1].id, act) for act in actions]
            coll = list(zip(actions, states_list))
            score = 0
            if max_levels == 0:
                return -len(coll) / 10
            for c in coll:
                c[1].adjust_win_loss()
                if c[1].is_win():
                    score = score - 1
                else:
                    if c[1].is_loss():
                        score = score + 1
                    else:
                        r = self.rekurzivna(c[1], 1, max_levels-1)
                        score = score - r

            return score / len(coll)


class MaxNAgent(StudentAgent):

    def get_next_action(self, state, max_levels):
        return self.odredi(state, max_levels)

    def odredi(self, state, max_levels):
        actions = self.get_legal_actions(state)

        states_list = [state.apply_action(self.id, act) for act in actions]
        coll = list(zip(actions, states_list))

        akcija = None
        vrednost = -math.inf
        listaPoraza = []
        for c in coll:
            c[1].adjust_win_loss()
            if c[1].is_win():
                return c[0]
            if c[1].is_loss():
                listaPoraza.append(c[0])
            else:
                niz = self.rekurzivna(c[1], 1, max_levels-1)
                if niz[0] == 1:
                    return c[0]
                if niz[0] == -1:
                    listaPoraza.append(c[0])
                else:
                    if vrednost < niz[0]:
                        vrednost = niz[0]
                        akcija = c[0]
        if vrednost > -1:
            return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NORTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NE':
                akcija = listaPoraza[i]
                return akcija
        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'EAST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SE':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SOUTH':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'SW':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'WEST':
                akcija = listaPoraza[i]
                return akcija

        for i in range(len(listaPoraza)):
            if listaPoraza[i] == 'NW':
                akcija = listaPoraza[i]
                return akcija

        return listaPoraza[0]

    def rekurzivna(self, state, index, max_level):
        nizR = []
        actions = state.agents[index].get_legal_actions(state)

        states_list = [state.apply_action(state.agents[index].id, act) for act in actions]

        coll = list(zip(actions, states_list))
        vrednost = -math.inf
        listaPoraza = []
        nizPom = []
        for i in range(len(state.agents)):
            nizPom.append(-1)

        nizPom[index] = 1
        nizR = nizPom
        if max_level == 0:
            for i in range(len(state.agents)):
                nizPom.append(len(state.agents[i].get_legal_actions(state)) /10)
            return nizPom
        for c in coll:
            c[1].adjust_win_loss()
            if c[1].is_win():
                return nizPom
            if c[1].is_loss():
                listaPoraza.append(c[0])
            else:
                niz = self.rekurzivna(c[1], (index + 1) % len(state.agents), max_level-1)
                if niz[index] == 1:
                    return niz

                if vrednost < niz[index]:
                    vrednost = niz[index]
                    nizR = niz

        return nizR
