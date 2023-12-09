import tkinter as tk
import csv

#Forewarning, I attempted to separate this code into three modules, but I kept getting circular import errors
#Not sure how you can jump from a logic handeling module to an api handeling module to a logic handeling module and etc .. etc.


class VotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting App")
        self.logged_in_user = None  # To track the logged-in user
        self.votecount = {"Cameron": 0, "Allison": 0, "Diego": 0}
        self.vote_button_created = False
        self.error_label = None
        self.load_initial_votes()
        self.create_login_gui()

    def create_login_gui(self):
        # Login frame
        login_frame = tk.Frame(self.root)
        login_frame.pack()

        # Username label and entry
        username_label = tk.Label(login_frame, text="Username:")
        username_label.pack()
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.pack()

        # Password label and entry label
        password_label = tk.Label(login_frame, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(
            login_frame, show="*"
        )  # Shows asterisks for password
        self.password_entry.pack()

        # the login button
        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.pack()

        exit_button = tk.Button(self.root, text="Exit", command=self.save_votes_and_exit)
        exit_button.pack()

    def load_initial_votes(self):
        #Loads initial votes to allow for proper iteration of voters and their votes
        try:
            with open("votes.csv", "r", newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row[0] in self.votecount:
                        self.votecount[row[0]] = int(row[1])
        except FileNotFoundError:
            pass

    def create_voting_gui(self):
        #Voting gui conditions
        if self.logged_in_user is not None and not self.vote_button_created:
            self.vote_button = tk.Button(self.root, text="Vote", command=self.show_vote_menu)
            self.vote_button.pack()
            self.vote_button_created = True


    def show_vote_menu(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("logins.csv", "r", newline="") as logins:
            csv_reader = csv.reader(logins)
            rows = list(csv_reader)
            #We need to access or csv file and mark users when they vote to restrict priviledges 

            for row in rows:
                if row[0] == username and row[1] == password:
                    rows[rows.index(row)].append("voted")
                    with open("logins.csv", "w", newline="") as writer:
                        csv_writer = csv.writer(writer)
                        csv_writer.writerows(rows)
                        break
                else:
                    pass

        if self.logged_in_user is not None:
            self.vote_menu_window = tk.Toplevel(self.root)
            self.vote_menu_window.title("Vote Menu")

            # Candidate buttons
            cameron_button = tk.Button(
                self.vote_menu_window, text="Cameron", command=lambda: self.vote("Cameron")
            )
            allison_button = tk.Button(
                self.vote_menu_window, text="Allison", command=lambda: self.vote("Allison")
            )
            diego_button = tk.Button(
                self.vote_menu_window, text="Diego", command=lambda: self.vote("Diego")
            )

            cameron_button.pack()
            allison_button.pack()
            diego_button.pack()
            #Packing candidate options

    def vote(self, candidate: str):
        self.votecount[candidate] += 1
        self.update_votes_file()
        self.vote_menu_window.destroy()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.vote_button.destroy()
        self.save_votes_and_exit()
        #I was going to allow for a portal to exist for all voters, but I realized that it is both easier and more convenient to just close the program
        #I just nuked everything
        self.logged_in_user = None

    def update_votes_file(self):
        #Iterating votes on top of votes that were already made in previous sessions
        with open("votes.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            for candidate, count in self.votecount.items():
                csv_writer.writerow([candidate, count])

    def save_votes_and_exit(self):
        #Left room for the possibility of resetting and reopening the iframe
        self.root.destroy()

    def login(self):
    # Check username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("logins.csv", "r", newline="") as logins:
            csv_reader = csv.reader(logins)
            rows = list(csv_reader)
            #Accessing csv to carry credential handeling logic shown below

            for row in rows:
                if row[0] == username and row[1] == password:
                    if len(row) >= 3:
                        if self.error_label:
                            self.error_label.destroy()
                            #I don't like it when a million error labels stack up
                            #It would be cool to add some kind of time based restriction for brute forcers

                        self.error_label = tk.Label(self.root, text="User already voted")
                        self.error_label.pack()
                        self.username_entry.delete(0, tk.END)
                        self.password_entry.delete(0, tk.END)
                        self.logged_in_user = None
                        return 

                    else:
                        # Mark the user as logged in
                        if self.error_label:
                            self.error_label.destroy()

                        with open("logins.csv", "w", newline="") as writer:
                            csv_writer = csv.writer(writer)
                            csv_writer.writerows(rows)

                        self.logged_in_user = username
                        self.create_voting_gui()
                        return  # Exit the function after successful login

            # If login is unsuccessful, display an error message
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            if self.error_label:
                self.error_label.destroy()

            self.error_label = tk.Label(self.root, text="Invalid username or password")
            self.error_label.pack()
            self.logged_in_user = None  # Resets the logged_in_user

                        




def main():
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
