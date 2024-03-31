import grpc
import random
import time
from concurrent import futures
import rps_pb2
import rps_pb2_grpc

class RockPaperScissorsServicer(rps_pb2_grpc.RockPaperScissorsServicer):
    def PlayGame(self, request, context):
        ai_move = random.randint(1, 3)  # Generate AI move
        move_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print("AI plays:", move_dict[ai_move])
        print("Human plays:", move_dict[request.player_move])
        # time.sleep(3)  # Simulate processing time
        winner = determine_winner(request.player_move, ai_move)  # Determine winner
        winner_dict = {0: "AI", 1: "Human", 2: "None"}
        print("Winner is ",winner_dict[winner])
        return rps_pb2.GameResponse(ai_move=ai_move, winner=winner)

def determine_winner(player_move, ai_move):
    # Rock: 1, Paper: 2, Scissors: 3
    if player_move == ai_move:
        return 2  # Tie
    elif (player_move == 1 and ai_move == 3) or \
         (player_move == 2 and ai_move == 1) or \
         (player_move == 3 and ai_move == 2):
        return 1  # Player wins
    else:
        return 0  # AI wins

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rps_pb2_grpc.add_RockPaperScissorsServicer_to_server(RockPaperScissorsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
