import grpc
import rps_pb2
import rps_pb2_grpc
import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import cvzone

def play_game(player_move):
    channel = grpc.insecure_channel('localhost:50051')
    stub = rps_pb2_grpc.RockPaperScissorsStub(channel)
    response = stub.PlayGame(rps_pb2.GameRequest(player_move=player_move))
    return response

if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors!")
    
    # Initialize OpenCV objects
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    detector = HandDetector(maxHands=1)
    
    # Variables for game state
    start_game = False
    initial_time = 0
    state_result = False
    scores = [0, 0]  # [AI, Player]

    while True:
        img_bg = cv2.imread("Resources/BG.png")
        success, img = cap.read()
        img_scaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        img_scaled = img_scaled[:, 80:480]
        
        # Find Hands
        hands, _ = detector.findHands(img_scaled)
        
        # Handle game logic
        if start_game:
            timer = time.time() - initial_time
            cv2.putText(img_bg, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            if timer > 3:
                state_result = True
                timer = 0

                if hands:
                    player_move = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        player_move = 1
                    elif fingers == [1, 1, 1, 1, 1]:
                        player_move = 2
                    elif fingers == [0, 1, 1, 0, 0]:
                        player_move = 3

                    # Send player's move to server
                    response = play_game(player_move)
                    ai_move = response.ai_move
                    winner = response.winner
                    imgAI = cv2.imread(f'Resources/{ai_move}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(img_bg, imgAI, (149, 310))

                    # Update scores based on server response
                    if winner == 0:
                        scores[0] += 1
                    elif winner == 1:
                        scores[1] += 1

                    # Reset game state
                    start_game = False
                    # state_result = s
        
        img_bg[234:654, 795:1195] = img_scaled
    
        if state_result:
            img_bg = cvzone.overlayPNG(img_bg, imgAI, (149, 310))
    
        cv2.putText(img_bg, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(img_bg, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    
        # cv2.imshow("Image", img)
        cv2.imshow("BG", img_bg)
        # cv2.imshow("Scaled", imgScaled)

        # Wait for 's' key to start the game
        key = cv2.waitKey(1)
        if key == ord('s'):
            start_game = True
            initial_time = time.time()
