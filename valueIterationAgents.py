# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        #Pseudocode:
        #V*(s)=max a of T(s,a,s')*(R(s,a,s')+gamma*V*(s'))
        #for action in a, calculate V*
        #going to recurse down
        #find best at end
        #self.values stores reference to future states?
        for i in range(iterations):
            for state in self.mdp.getStates():
                self.valueIterationHelper(state)


    # calculate just the path given info
    #put into new counter



    def valueIterationHelper(self, state):
        if self.mdp.isTerminal(state):
            return
        max = None
        for a in self.mdp.getPossibleActions(state):
            probs = self.mdp.getTransitionStatesAndProbs(state,a)
            V=0
            for key in range(len(probs)):
                print(probs[key][1])
                print(probs[key][0])
                reward = probs[key][1]*(self.mdp.getReward(state,a,probs[key][0])+self.discount*self.values[probs[key][0]])
                V += reward
            if V>max or max == None:
                max = V
        self.values[state] = max





    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        Q=0
        probs = self.mdp.getTransitionStatesAndProbs(state,a)
        for index in len(probs):
            self.valueIterationHelper(probs[i][0], completedIterations+1)
            reward = probs[index][1](self.mdp.getReward(state,a,probs[index][0])+self.discount*self.values[probs[index][0]])
            Q += reward
        return Q


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        actions = util.Counter()
        for a in self.mdp.getPossibleActions(state):
            V = 0
            probs = self.mdp.getTransitionStatesAndProbs(state,a)
            for index in range(len(probs)):
                reward = probs[index][1]*(self.mdp.getReward(state,a,probs[index][0])+self.discount*self.values[probs[index][0]])
                V += reward
            actions[a]=V
        return actions.argMax()


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
